import psycopg2
import datetime

ClearSaleConversionDict = {
    'REX-CLIENT-5a380953a39d5502235fc966': 0.89,
    'REX-CLIENT-5a38096d7fe96a01c581a706': 0.88,
    'REX-CLIENT-5a38098da39d5502765fc96f': 0.88,
    'REX-CLIENT-5a380a66a39d5503025fc973': 0.91,
    'REX-CLIENT-5a380aa8a39d5503535fc967': 1,
    'REX-CLIENT-5a380ac7a39d5503535fc97c': 0.76,
    'REX-CLIENT-5a380ae2d1379e03a933a0a9': 0.74,
    'REX-CLIENT-5a380b37a39d5503c45fc962': 0.94,
    'REX-CLIENT-5a380b5f14a0c00404be1b82': 0.93,
    'REX-CLIENT-5a380b7ad1379e042233a0ad': 0.77,
    'REX-CLIENT-5a380b9d14a0c0044dbe1b80': 0.7,
    'REX-CLIENT-5a380bb2a39d5503fe5fc964': 0.82,
    'REX-CLIENT-5a380bcbd1379e03e633a0a9': 0.78,
    'REX-CLIENT-5a380cf27fe96a047581a71a': 0.93,
    'REX-CLIENT-5a380db47fe96a05e881a6f3': 0.83,
    'REX-CLIENT-5a380dd57fe96a059081a6f2': 0.93,
    'REX-CLIENT-5a380e267fe96a059081a6fb': 0.77,
    'REX-CLIENT-5a380f84d1379e068d33a0ad': 0.9,
    'REX-CLIENT-5a380fb2d1379e06fc33a0a9': 0.75,
    'REX-CLIENT-5a381009a39d5506a75fc96f': 0.94,
    'REX-CLIENT-5a381035a39d5506a75fc972': 0.79,
    'REX-CLIENT-5a2fc6735a99e6085e866cd7': 0.94,
    'REX-CLIENT-5a3810807fe96a075781a6fd': 0.65,
    'REX-CLIENT-5a38112514a0c007b1be1b85': 0.95,
    'REX-CLIENT-5a3811f3d1379e086233a0ba': 0.68,
    'REX-CLIENT-5a38120c14a0c0088dbe1b82': 0.97,
    'REX-CLIENT-5a3812227fe96a08ec81a6f0': 0.87,
    'REX-CLIENT-5a38123ad1379e086233a0c5': 0.86,
    'REX-CLIENT-5a3812a37fe96a08ec81a702': 0.94,
    'REX-CLIENT-5a38138fa39d5509835fc962': 0.79,
    'REX-CLIENT-5a381378d1379e08e433a0d9': 0.76,
    'REX-CLIENT-5a3813a714a0c00932be1b8f': 0.98,
    'REX-CLIENT-5a3813bca39d5509245fc972': 0.9,
    'REX-CLIENT-5a381422a39d550a1c5fc966': 0.72,
    'REX-CLIENT-5a38153d7fe96a0b0d81a6fa': 0.82,
    'REX-CLIENT-5a3815ed14a0c00addbe1b88': 0.82,
    'REX-CLIENT-5a381622d1379e0b8733a0ab': 0.83,
    'REX-CLIENT-5a3816377fe96a0bdd81a6f2': 0.8,
    'REX-CLIENT-5a3816927fe96a0bb981a6f0': 0.95,
    'REX-CLIENT-5a3816ed7fe96a0c4c81a6f8': 0.3,
    'REX-CLIENT-5a38181414a0c00ca9be1b9b': 0.09,
    'REX-CLIENT-5a2fc6185a99e6085e866cd2': 0.76,
    'REX-CLIENT-5a3818d314a0c00deabe1b8a': 0.82,
    'REX-CLIENT-5a3825d99fa4370a7996ad3c': 0.86,
    'REX-CLIENT-5a3909beb98832718dae0f05': 0.9,
    'REX-CLIENT-5a382618acf5dd0b8c7eede9': 0.44,
    'REX-CLIENT-5a3909383ef0086db3909c16': 0.72,
    'REX-CLIENT-5a3908fe3ef0086d56909c19': 0.76,
    'REX-CLIENT-5a382baaacf5dd102e7eede3': 0.49,
    'REX-CLIENT-5a381abe8318540102a9d599': 0.83,
    'REX-CLIENT-5a38253cacf5dd0a8e7eee01': 0.78,
    'REX-CLIENT-5a3825819fa4370a7996ad37': 0.42,
    'REX-CLIENT-5a3825a0acf5dd0b597eede5': 0.6,
    'REX-CLIENT-5a38266eacf5dd0b8c7eedf4': 0.78,
    'REX-CLIENT-5a3826c08318540a52a9d591': 0.62,
    'REX-CLIENT-5a3827369fa4370b2996ad2f': 0.83,
    'REX-CLIENT-5a38278cacf5dd0c8f7eede1': 0.85,
    'REX-CLIENT-5a3827a78318540b12a9d595': 0.83,
    'REX-CLIENT-5a3828319fa4370c3896ad1d': 0.52,
    'REX-CLIENT-5a382a9f9fa4370dc596ad4f': 0.8,
    'REX-CLIENT-5a382b4f8318540db2a9d59d': 0.67,
    'REX-CLIENT-5a382b61acf5dd0f7c7eedf8': 0.87,
    'REX-CLIENT-5a382b779fa4370ec296ad27': 0.81,
    'REX-CLIENT-5a382b886ad1f90e5859ad13': 0.85,
    'REX-CLIENT-5a382c00acf5dd102e7eedec': 0.76,
    'REX-CLIENT-5a382c56acf5dd106d7eede3': 0.21,
    'REX-CLIENT-5a382c718318540eb8a9d597': 0.77,
    'REX-CLIENT-5a382cdc8318540e83a9d5a7': 0.82,
    'REX-CLIENT-5a382cfeacf5dd11337eede1': 0.85,
    'REX-CLIENT-5a382d1bacf5dd11017eede8': 0.83,
    'REX-CLIENT-5a382d6dacf5dd11627eedeb': 0.8,
    'REX-CLIENT-5a382dca9fa43710c996ad27': 0.82,
    'REX-CLIENT-5a382decacf5dd12467eede5': 0.82,
    'REX-CLIENT-5a39088864635f6a9dd2ad4d': 0.78,
    'REX-CLIENT-5a3908a364635f6ac4d2ad4d': 0.71,
    'REX-CLIENT-5a3908d1b9883270baae0f0a': 0.32,
    'REX-CLIENT-5a3908e83ef0086d56909c16': 0.45,
    'REX-CLIENT-5a3909203fa3796d43cb0b71': 0.82,
    'REX-CLIENT-5a3909aa64635f6b55d2ad52': 0.81,
}


def QueryGroup(GroupId):
    hostname = 'rexlab-scooby-replica-a.cujsiitttsed.us-east-1.rds.amazonaws.com'
    username = 'lpincerato'
    password = 'C3f2dUjVWdSk5reQ'
    database = 'ScoobyDB'
    query = f"select client_key from \"Client\" c where group_id = {GroupId}"

    connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = connection.cursor()
    cur.execute(query)
    clientlist = cur.fetchall()
    connection.close()

    return clientlist



def QueryTransactions(RexClient, InitialDate, FinalDate):
    hostname = 'rexlab-scooby-replica-a.cujsiitttsed.us-east-1.rds.amazonaws.com'
    username = 'lpincerato'
    password = 'C3f2dUjVWdSk5reQ'
    database = 'ScoobyDB'
    query = \
        f"select order_json " \
        f"from \"Order\" o left join \"Client\" c on o.client_id = c.id " \
        f"where c.client_key = '{RexClient}' " \
        f"and o.created_at between cast('{InitialDate}' as TIMESTAMP) and cast('{FinalDate}' as TIMESTAMP)"
    connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = connection.cursor()
    cur.execute(query)
    transactionslist = cur.fetchall()
    connection.close()
    return list(sum(transactionslist, ()))



def CalculateConversion(Threshhold, TransactionList):

    total = len(TransactionList)
    approved = sum(1 for transaction in TransactionList if float(transaction['source']['antifraud_status']['score']) <= Threshhold/100)

    print(f"\n\nThreshhold é {Threshhold}")
    print(f"total é {total}")
    print(f"approved é {approved}")

    try:
        conv = approved/total
    except ZeroDivisionError:
        conv = 0

    return conv



def BestScore(RexClient):

    initialDate = "2018-01-18 00:00"
    finalDate = str(datetime.datetime.now())
    transactions = QueryTransactions(RexClient, initialDate, finalDate)

    # print(f"initialDate é {initialDate}")
    # print(f"finalDate é {finalDate}")
    # print(f"trx é {transactions}")
    # print(f"clearSale Score é {ClearSaleConversionDict.get(RexClient)}")

    try:
        clearSaleConversion = ClearSaleConversionDict.get(RexClient)
    except KeyError:
        print(f"A loja de chave {RexClient} não existe no dicionário de scores de referência!")
        clearSaleConversion = 0

    for x in range(100):
        conv = CalculateConversion(x, transactions)
        if conv >= clearSaleConversion:
            return x, len(transactions)

    return 0



def main():

    BestScoreTupleList = []

    clientList = QueryGroup(15)
    for client in clientList:
        bestscore = BestScore(client[0])
        BestScoreTupleList.append([client, bestscore[0], [1]])
        print(f"O Score do cliente {client} é {bestscore[0]} com {bestscore[1]} transações")

    print("Acabei, segue abaixo lista de scores: \n\n", BestScoreTupleList)

    return








################# ENTRY POINT ##################
main()
################################################