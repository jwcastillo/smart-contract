"""
BlockAuth smart contract v0.3.0 - https://blockauth.cc
"""

from boa.blockchain.vm.Neo.Runtime import Log, CheckWitness
from boa.blockchain.vm.Neo.Storage import Put, GetContext
from boa.code.builtins import concat

def Main(verification_values: str, address: str) -> int:
    """Entry point for the smart contract.

    Args:
        verification_values (str):
            string holding a GUID and a challenge value.
        address             (str):
            NEO address of sender.

    Return:
        (boolean): true or false to if the smart contract succeeded.
    """

    if len(verification_values) != 46:
        Log("Parameter must be 46 characters long")
        Log(verification_values)
        return 101

    guid = verification_values[0:36]
    if not IsGUID(guid):
        Log("Parameter first part must be a valid GUID")
        Log(guid)
        return 102

    challenge = verification_values[37:46]
    if not IsChallenge(challenge):
        Log("Parameter second part must be a valid challenge")
        Log(challenge)
        return 103

    from_is_sender = CheckWitness(address)
    if not from_is_sender:
        Log("Address parameter does not match sender address")
        Log(address)
        return 104

    context = GetContext()
    key = GenerateKey(guid, address)

    Put(context, key, challenge)

    return 200

def GenerateKey(guid, address: str) -> str:
    """Concatenate arguments for use as storage key.

    Args:
        guid    (str):
            GUID taken from smart contract argument.
        address (str):
            public NEO address of who invoked smart contract.

    Return:
        (str): args concatenated together with a '.' between each value.
    """

    with_period = concat(guid, '.')
    return concat(with_period, address)

def IsChallenge(challenge: str) -> bool:
    """Verifies a string has the following format: 'xxxx-xxxx'.

    Args:
        challenge (str): 
            value that needs to be verified.

    Return:
        (boolean): true or false to if the value is valid.
    """

    if len(challenge) != 9:
        return False

    if not IsDash(challenge, 4):
        return False 

    return True

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

def IsGUID(guid: str) -> bool:
    """Verifies a string has the following (GUID) format:
        'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'.

    Args:
        guid (str): 
            value that needs to be verified.

    Return:
        (boolean): true or false to if the value is valid.
    """

    if len(guid) != 36:
        return False

    if not IsDash(guid, 8):
        return False

    if not IsDash(guid, 13):
        return False

    if not IsDash(guid, 18):
        return False

    if not IsDash(guid, 23):
        return False

    return True