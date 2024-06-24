from . import rpc
from . import crypto

def create_account():

    wallet_id = rpc.wallet_create()
    accounts_id = rpc.accounts_create(wallet_id, 2)

    private_key = crypto.generate_private_key()
    public_key = rpc.key_expand(private_key)

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
