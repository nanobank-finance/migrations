import requests
import logging
from typing import Union, List, TypedDict

rpc_network = "http://127.0.0.1:17076"
session = requests.Session()

def wallet_create() -> Union[str, None]:
    """
    Creates a new wallet

    Returns:
        Union[str, None]: The wallet ID if successful
    """
    
    response = session.post(rpc_network, json={
        "action": "wallet_create",
        "password": "123",
    }).json()

    try:
        wallet_id = response["wallet"]
        print("wallet_id: ", wallet_id)
    except KeyError:
        logging.exception(response["error"])
        return
    
    return wallet_id

def accounts_create(wallet_id: str, count: int = 1) -> Union[List[str], None]:
    """
    Create accounts for a wallet

    Args:
        wallet_id (str): Created in wallet_create()
        count (int): Number of accounts to create for the wallet. Defaults to 1.

    Returns:
        Union[List[str], None]: The new account IDs if successful
    """

    response = session.post(rpc_network, json={
        "action": "accounts_create",
        "wallet": wallet_id,
        "count": count
    }).json()

    try:
        accounts_id = response["accounts"]
        print("accounts_id: ", accounts_id)
    except KeyError:
        logging.exception(response["error"])
        return
    
    return accounts_id


def key_expand(private_key: str) -> Union[str, None]:
    """
    Derive the public key from the private key

    Args:
        private_key (str): Key generated from crypto.generate_private_key()

    Returns:
        Union[str, None]: The public key if successful
    """


    response = session.post(rpc_network, json={
        "action": "key_expand",
        "key": private_key
    }).json()

    try:
        public_key = response["public"]
        print("public_key: ", public_key)
    except KeyError:
        logging.exception(response["error"])
        return
    
    return public_key
    

def wallet_add(wallet_id: str):
    from . import crypto
    private_key = crypto.generate_private_key()
    public_key = key_expand(private_key)
