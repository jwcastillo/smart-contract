"""
BlockAuth - NEO smart contract - https://blockauth.cc
"""

VERSION = "2.0.0"

from boa.blockchain.vm.Neo.Runtime import Log
from boa.blockchain.vm.Neo.Storage import GetContext, Put
from boa.blockchain.vm.Neo.Transaction import GetHash
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer
from boa.code.builtins import concat

def Main(key, challenge: str) -> int:
    """Entry point for the smart contract.

    Args:
        key       (str):
            UUID used within Storage key.
        challenge (str):
            UUID used within Storage key and value.

    Return:
        (int): status code representing if execution was a success.
    """

    if not IsUUID(key):
        Log("'key' parameter has an invalid RFC UUID format")
        Log(key)
        return 101

    if not IsUUID(challenge):
        Log("'challenge' parameter has an invalid RFC UUID format")
        Log(challenge)
        return 102

    context = GetContext()
    storageKey = GenerateStorageKey(key, challenge)
    
    transactionHash = GetTransactionHash()
    if len(transactionHash) == 0:
        Log("Transaction hash has a length of 0")
        return 103

    Put(context, storageKey, transactionHash)

    return 200

def GetTransactionHash() -> str:
    """Fetches the hash of the current transaction.

    Return:
        (str): hash of current transaction.
    """

    transaction = GetScriptContainer()
    hash = GetHash(transaction)
    return hash

def GenerateStorageKey(s1, s2: str) -> str:
    """Concatenate arguments for use as storage key.
    
    Args:
        s1 (str):
            first string to be used in concatenation.
        s2 (str):
            second string to be used in concatenation.

    Return:
        (str): args concatenated together with a '.' between each value.
    """

    withPeriod = concat(s1, '.')
    return concat(withPeriod, s2)

def IsDash(s: str, index: int) -> bool:
    """Verifies that character at index of string is '-'.

    Args:
        s     (str): 
            string to be examined.
        index (int):
            starting index of the possible '-' character.

    Return:
        (boolean): true or false to if the value is valid.
    """

    return s[index:index + 1] == '-'

def IsUUID(uuid: str) -> bool:
    """Verifies a string has the following valid RFC UUID format:
        'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'.

    Args:
        uuid (str): 
            value that needs to be verified.

    Return:
        (boolean): true or false to if the value is valid.
    """

    if len(uuid) != 36:
        return False

    if not IsDash(uuid, 8):
        return False

    if not IsDash(uuid, 13):
        return False

    if not IsDash(uuid, 18):
        return False

    if not IsDash(uuid, 23):
        return False

    return True