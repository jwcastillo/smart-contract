# v0.1.0
# Author: @revett

from boa.blockchain.vm.Neo.Output import GetScriptHash
from boa.blockchain.vm.Neo.Storage import GetContext, Put
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer
from boa.code.builtins import concat

# Main is the entry point to the smart contract.
# --
# @param {string} verification_values - string holding a GUID and a challenge value.
# @return {boolean} - true or false to if the smart contract succeeded.
def Main(verification_values):
    # Verify length of input argument is valid
    if len(verification_values) != 46:
        return False

    # Extract and verify the application GUID
    app_guid = verification_values[0:36]
    if not IsGUID(app_guid):
        return False

    # Extract and verify the challenge string
    challenge = verification_values[37:46]
    if not IsChallenge(challenge):
        return False

    # Fetch sender public address, and check if blank value (error) is returned
    public_address = GetPublicAddress()
    if public_address == '':
        return False

    # Populate values needed for storage.Put() function call
    context = GetContext()
    key = GenerateKey(app_guid, public_address)

    # Store value, and return
    Put(context, key, challenge)
    return True

# GenerateKey takes two strings as arguments, concatenates each values together to form
# a single string to return. This value is used as the storage key.
# --
# @param {string} app_guid - application GUID taken from smart contract argument.
# @param {string} public_address - public NEO address of who invoked smart contract.
# @return {string} - both arguments concatenated together with a '.' between each value.
def GenerateKey(app_guid, public_address):
    with_period = concat(app_guid, '.')
    return concat(with_period, public_address)

# GetPublicAddress retrieves the NEO public address of the user who invoked the smart
# contract.
# --
# @return {string} - public NEO address corresponding to who invoked the smart contract.
def GetPublicAddress():
    transaction = GetScriptContainer()
    references = transaction.References

    if len(references) < 1:
        return ""

    reference = references[0]
    return GetScriptHash(reference)

# IsChallenge verifies that a string has the following format: 'xxxx-xxxx'.
# --
# @param {string} challenge - value that needs to be verified.
# @return {boolean} - true or false to if the value is valid.
def IsChallenge(challenge):
    return len(challenge) == 9 and challenge[4:5] == '-'

# IsGUID verifies that a string has the following (GUID) format:
# 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
# --
# @param {string} guid - value that needs to be verified.
# @return {boolean} - true or false to if the value is valid.
def IsGUID(guid):
    if len(guid) != 36:
        return False

    dash_indexes = [8, 13, 18, 23]
    for dash_index in dash_indexes:
        if guid[dash_index:dash_index+1] != '-':
            return False

    return True
