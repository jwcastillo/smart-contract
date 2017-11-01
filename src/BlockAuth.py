"""
BlockAuth smart contract, written in Python and compiled using neo-boa.
v0.2.0
https://blockauth.cc
"""

from boa.blockchain.vm.Neo.Output import GetScriptHash
from boa.blockchain.vm.Neo.Storage import GetContext as GetStorageContext
from boa.blockchain.vm.Neo.Storage import Put as StoragePut
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer
from boa.code.builtins import concat


def main(verification_values: str) -> bool:
    """Entry point for the smart contract.

    Args:
        verification_values (str):
            string holding a GUID and a challenge value.

    Return:
        (boolean): true or false to if the smart contract succeeded.
    """

    if len(verification_values) != 46:
        return False

    app_guid = verification_values[0:36]
    if not is_guid(app_guid):
        return False

    challenge = verification_values[37:46]
    if not is_challenge(challenge):
        return False

    public_address = get_public_address()
    if public_address == '':
        return False

    context = GetStorageContext()
    key = generate_key(app_guid, public_address)

    StoragePut(context, key, challenge)
    return True


def generate_key(app_guid, public_address: str) -> str:
    """Concatenate arguments for use as storage key.

    Args:
        app_guid       (str):
            application GUID taken from smart contract argument.

        public_address (str):
            public NEO address of who invoked smart contract.

    Return:
        (str): args concatenated together with a '.' between each value.
    """

    with_period = concat(app_guid, '.')
    return concat(with_period, public_address)


def get_public_address() -> str:
    """Retrieves NEO public address of user who invoked the smart contract.
    
    Return:
        (str): NEO public address, or empty if error.
    """

    transaction = GetScriptContainer()
    references = transaction.References

    if len(references) < 1:
        return ""

    reference = references[0]
    return GetScriptHash(reference)


def is_challenge(challenge: str) -> bool:
    """Verifies a string has the following format: 'xxxx-xxxx'.

    Args:
        challenge (str): 
            value that needs to be verified.

    Return:
        (boolean): true or false to if the value is valid.
    """

    return len(challenge) == 9 and challenge[4:5] == '-'


def is_guid(guid: str) -> bool:
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

    dash_indexes = [8, 13, 18, 23]
    for dash_index in dash_indexes:
        if guid[dash_index:dash_index+1] != '-':
            return False

    return True