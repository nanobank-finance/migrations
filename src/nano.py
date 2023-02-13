import schemas
import requests

nano_currency = "http://127.0.0.1:17076"
session = requests.Session()

""" lower level utilities """

def create_account():
    # https://docs.nano.org/commands/rpc-protocol/#account_create
    response = session.post(nano_currency, json={
        "action": "telemetry"
    })

    print(response.__dict__)

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

def test_faucet_deposit(wallet: schemas.Wallet):
    pass

def test_faucet_withdraw(wallet: schemas.Wallet):
    pass

def cleanup_test_wallets():
    pass
