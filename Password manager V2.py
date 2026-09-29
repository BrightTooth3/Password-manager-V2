import math
import hashlib
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def generateHashedDataHex():
    data = ''
    for i in range(16):
        data += random.choice(alphabet)

    hashFunction = hashlib.sha3_512()  # - Sets and creates the hashing function, and stores it in this variable i named HashFunction
    myVariable = data  # - data to be hashed
    myVariable = myVariable[
        0].encode()  # - encodes myVariable with utf-8 and changes the text to its byte code representation. The data needs to be utf-8 for the HashFunction to use it, but python strings are Unicode text by default. Also make sure the data being encoded is a string (not a list or something) otherwise it wont accept it.
    hashFunction.update(myVariable)  # - loads myVariable into the hashFunction and runs it
    hashedDataHex = hashFunction.hexdigest()  # - hexdigest is what actually fetches and returns the hash data as a Hex string
    return hashedDataHex

for i in range(5):
    print(generateHashedDataHex())