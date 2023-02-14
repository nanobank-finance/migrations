from . import rpc

def create_account():

    wallet_id = rpc.wallet_create()
    accounts_id = rpc.accounts_create(wallet_id, 2)
    rpc.wallet_add(wallet_id)

    # # get the wallet address

    # response = session.post(nano_currency, json={
    #     "action": "account_get",  
    #     "key": wallet
    # }).json()

    # try:
    #     account = response["account"]
    # except KeyError:
    #     logging.exception(response["error"])
    #     return
    
    # add the wallet

    # response = session.post(nano_currency, json={
    #     "action": "wallet_add",
    #     "wallet": wallet_id,
    #     "key": account
    # }).json()


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
