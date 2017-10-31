"""
BlockAuth smart contract, written in Python and compiled using neo-boa.
v0.2.0
https://blockauth.cc
"""

from boa.blockchain.vm.Neo.Output import GetScriptHash as get_script_hash
from boa.blockchain.vm.Neo.Storage import GetContext as get_storage_context
from boa.blockchain.vm.Neo.Storage import Put as storage_put
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer as get_script_container
from boa.code.builtins import concat

def main(verification_values):
    """
        main() is the entry point for the smart contract.

        Args:
            verification_values (string): string holding a GUID and a challenge value.
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

    context = get_storage_context()
    key = generate_key(app_guid, public_address)

    storage_put(context, key, challenge)
    return True

def generate_key(app_guid, public_address):
    """
        generate_key() concatenates each argument (strings) together to form a single
        string, which is then used as the storage key.

        Args:
            app_guid       (string): application GUID taken from smart contract argument.
            public_address (string): public NEO address of who invoked smart contract.
        Return:
            (string): both arguments concatenated together with a '.' between each value.
    """

    with_period = concat(app_guid, '.')
    return concat(with_period, public_address)

def get_public_address():
    """
        get_public_address() retrieves the NEO public address of the user who invoked the
        smart contract.

        Return:
            (string): public NEO address corresponding to who invoked the smart contract.
    """

    transaction = get_script_container()
    references = transaction.References

    if len(references) < 1:
        return ""

    reference = references[0]
    return get_script_hash(reference)

def is_challenge(challenge):
    """
        is_challenge() verifies that a string has the following format: 'xxxx-xxxx'.

        Args:
            challenge (string): value that needs to be verified.
        Return:
            (boolean): true or false to if the value is valid.
    """

    return len(challenge) == 9 and challenge[4:5] == '-'

def is_guid(guid):
    """
        is_guid() verifies that a string has the following (GUID) format:
        'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'.

        Args:
            guid (string): value that needs to be verified.
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
