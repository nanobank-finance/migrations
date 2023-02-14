import requests
import logging
from google.protobuf.json_format import MessageToDict

nano_currency = "http://127.0.0.1:17076"
session = requests.Session()

def create_account():

    # create the wallet key

    response = session.post(nano_currency, json={
        "action": "wallet_create"
    }).json()

    try:
        wallet = response["wallet"]
    except KeyError:
        logging.exception(response["error"])
        return
    
    # get the wallet address

    response = session.post(nano_currency, json={
        "action": "account_get",  
        "key": wallet
    }).json()

    try:
        account = response["account"]
    except KeyError:
        logging.exception(response["error"])
        return

    print(account)

def transfer(address_to, address_from):
    # https://docs.nano.org/commands/rpc-protocol/#send
    pass

def get_balance(address):
    # https://docs.nano.org/commands/rpc-protocol/#wallet_balances
    pass

def get_transaction_history(address):
    # https://docs.nano.org/commands/rpc-protocol/#wallet_history
    pass

""" higher level utilities """

def test_faucet_deposit(wallet):
    pass

def test_faucet_withdraw(wallet):
    pass

def cleanup_test_wallets():
    pass
