import requests
import psycopg2


def patch_konduto_key(api_key, client_key):
    url = f"https://register.rexlab.com.br/client/{client_key}"
    paramsKey = dict(
        api_key = api_key
    )
    params = dict(
        external_identifiers = paramsKey
    )
    headers = {"Authorization": "b1ed8828-097e-421d-baed-bb3e464b39aa"}

    req = requests.patch(url, json=params, headers=headers, verify=False)

    return req.json()

def get_rex_client_list():
    hostname = 'rexlab-scooby-replica-a.cujsiitttsed.us-east-1.rds.amazonaws.com'
    username = 'lpincerato'
    password = 'C3f2dUjVWdSk5reQ'
    database = 'ScoobyDB'
    query = "select client_key from \"Client\" c where c.group_id = 15"

    connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = connection.cursor()
    cur.execute(query)
    keyList = cur.fetchall()
    connection.close()

    return keyList


def main():

    new_api_key = 'PE45CC004C0941C9F6BC0'
    keyList = get_rex_client_list()

    #Debug
    # resp = patch_konduto_key(new_api_key, keyList[0][0])
    # print(resp)

    for client_key in keyList:
        print(f"O Client {client_key[0]} teve sua chave alterada\n")
        response = patch_konduto_key(new_api_key, client_key[0])
        print(response)


main()