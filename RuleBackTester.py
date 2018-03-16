import sys
import json
import csv
import psycopg2
import boto3
import datetime
import os
import logging
from queue import Queue
from threading import Thread

from config.config import Config
from config.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from config.credentials import USER
from antifraud_config_loader import AntifraudConfigLoader


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

################################## PARÂMETROS ####################################
rexkey = 'REX-CLIENT-59cd6fe36f731f476de1c0b1'                                                                           # Client_Key ou Group_Key
rulefilepath = r'C:\Users\lpincerato\rules\Ipiranga\PYTHON-REX-CLIENT-59cd6fe36f731f476de1c0b1.py'     # Diretório da regra a ser testada
initialdate = datetime.date(2018, 2, 1)                                                                                        # Data Inicial
finaldate = datetime.datetime.now()                                                                                             # Data Final
csv_path = r"C:/Users/lpincerato/Desktop/Rule_tester.csv"                                                                       # Diretório para salvamento do csv
################################## PARÂMETROS ####################################


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')
# Restore
def enablePrint():
    sys.stdout = sys.__stdout__
def get_orders(isclient, rexkey, initialdate, finaldate):
    hostname = 'rexlab-scooby-replica-a.cujsiitttsed.us-east-1.rds.amazonaws.com'
    username = 'lpincerato'
    password = 'C3f2dUjVWdSk5reQ'
    database = 'ScoobyDB'
    param = 'c.client_key'

    if not isclient:
        param = 'g.group_key'

    query = f'''select order_json ->> 'source'  from "Order" o join "Client" c on o.client_id = c.id join "Group" g on c.group_id = g.id where {param} = '{rexkey}' and o.created_at between '{initialdate}'::timestamp and '{finaldate}'::timestamp'''

    print("\nIniciando execução da query de busca das transações")

    connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = connection.cursor()
    cur.execute(query)
    orderList = cur.fetchall()
    connection.close()

    print("Finalizada execução da query de busca das transações")

    return list(sum(orderList, ()))
def test_sample(orders, rulefilepath):
    from connectors.bigbrother_connector import BigBrotherServiceConnector
    from connectors.bureau import Bureau
    from connectors.google_maps import GoogleMaps

    tested_order_list = list()

    estimated_order_time = 5 # Em segundos

    #debug
    print(f"\niniciando aplicação da regra nas transações, serão testadas {len(orders)} transações")

    rules = open(rulefilepath, encoding='latin-1').read()

    for order in orders:

        secETC = ((len(orders) - (orders.index(order)+1)) * estimated_order_time)
        minETC = secETC /60

        print(f"iniciando teste da transação {orders.index(order)+1}/{len(orders)} | Tempo estimado até finalizar: {secETC} segundos ({minETC} minutos) ")

        order = json.loads(order)
        AntifraudConfigLoader.load(order)

        decision = {
            'action': '',
            'reasons': list()
        }

        blockPrint()
        logging.getLogger('botocore').setLevel(logging.CRITICAL)
        logging.getLogger('urllib3').setLevel(logging.CRITICAL)
        logging.getLogger('pyrules').setLevel(logging.CRITICAL)
        # logger.disabled = True
        exec(rules, locals())
        # logger.disabled = False
        enablePrint()

        cbk = False
        if order['payment']['status'] == 'chargedback': cbk = True

        tested_order = {
            'orderid': order['order_id'],
            'status': decision['action'],
            'reasons': decision['reasons'],
            'amount': order['payment']['total_amount'],
            'chargeback': cbk,
            'order': order
        }

        tested_order_list.append(tested_order)

    return tested_order_list
def calculate_results(tested_order_list):

    totalnumber = len(tested_order_list)
    totalamount = 0
    for order in tested_order_list:
        totalamount += order['amount']
    approved = sum(1 for order in tested_order_list if order['status'] == 'approve')
    chargeback = sum(1 for order in tested_order_list if order['chargeback'] == True)
    forward = sum(1 for order in tested_order_list if order['status'] == 'forward')

    conversion = approved / totalnumber
    chargeback = chargeback / totalnumber
    manual = forward / totalnumber
    auto = 1-(forward / totalnumber)

    result = {
            'totalnumber': totalnumber,
            'totalamount': totalamount/100,
            'conversionindex': conversion,
            'chargebackindex': chargeback,
            'manualindex': manual,
            'autoindex': auto
        }

    return result
def main():

    # rexkey = input('Insira a chave Rex (client ou group key): ')
    isclient = True

    # testa se a chave inputada é de um client ou de um grupo
    if 'REX-GROUP' in rexkey:
        isclient = False

    # Pega todas as orders do cliente no período
    orders = get_orders(isclient, rexkey, initialdate, finaldate)

    # Passa as orders pela regra
    tested_order_list = test_sample(orders,rulefilepath)


    with open(csv_path, 'w') as out:
        csv_out = csv.writer(out, lineterminator='\n')
        csv_out.writerow(['Order Id', 'Decisão', 'Motivos', 'Valor', 'IsChargeback'])
        for order in tested_order_list:
            order['reasons'] = ' | '.join(order['reasons'])
            csv_out.writerow(order.values())

    # Escreve no csv
    # with open(csv_path, 'w') as out:
    #     fields = tested_order_list[0]
    #     csv_out = csv.DictWriter(out,fieldnames=fields,lineterminator = r'\n')
    #     csv_out.writerow(['Order Id', 'Decisão', 'Motivos', 'Valor', 'IsChargeback'])
    #     for order in tested_order_list:
    #         order['reasons'] = ' | '.join(order['reasons'])
    #
    #         csv_out.writerow(order.values())

    # Calcula KPIs
    result = calculate_results(tested_order_list)

    print(f'\n\nDiagnóstico completo (Avaliadas {result["totalnumber"]} transações e R$ {result["totalamount"]}).\nResultados abaixo:\n\nConversão: {str(float(result["conversionindex"])*100)+"%"}\nChargeback: {str(float(result["chargebackindex"])*100)+"%"}\nDecisão Auto: {str(float(result["autoindex"])*100)+"%"}\nDecisão Manual: {str(float(result["manualindex"])*100)+"%"}')

    return


################# ENTRY POINT ##################
print("Iniciando (Versão 1.1)")
main()
print("Processo finalizado!")
################################################