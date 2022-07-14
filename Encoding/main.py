#!/usr/bin/env python3

# Convert character ords back for UTF-8
ord = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for i in ord:
    print("".join(chr(i)))

# Decode hex to bytes
from pwn import *

hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
ascii = unhex(hex)
# OR
ascii = bytes.fromhex(hex) # Using built ins
print(ascii)

# Decode from hex to bytes with pwntools, then decode base64 to UTF-8
import base64
from pwn import *

hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes = unhex(hex)
b64 = base64.b64encode(bytes)
print(b64)

# Long ints to bytes with "PyCryptodome" library
# pip3 install PyCryptodome
from Crypto.Util.number import *

int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(int))
