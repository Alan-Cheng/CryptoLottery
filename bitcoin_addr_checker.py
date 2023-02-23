#fuction to check the bitcon address

import hashlib
import base58
import binascii
import re

def check_bitcoin_address(address):
    #decode the base58 address to hex
    decode = base58.b58decode(address)
    #split the hex into two parts, the last 4 bytes are the checksum
    decode, checksum = decode[:-4], decode[-4:]
    #hash the decode hex 2 times with sha256
    hash_decode = hashlib.sha256(hashlib.sha256(decode).digest()).digest()
    #check if the checksum is the same as the first 4 bytes of the hash_decode
    if checksum == hash_decode[:4]:
        return True
    else:
        return False

def check_format(string):
    format = "^[0-9a-zA-Z]{34}$"
    if re.match(format, string):
        return True
    else:
        return False
