#!/usr/bin/env python

from ctypes import CDLL
from Crypto.Cipher import AES

libc = CDLL("libc.so.6")

block_base = 0x5060
xor_key_addr = 309876

f = open("dump", "rb")
data = f.read()

flag_block = data[block_base: block_base + 128]

# 1614445200 : 2021/02/27 17:00 CST
for ts in range(1614445200, 0, -1):
    libc.srand(ts)
    
    offset = 128
    for _ in range(0, 64):
        offset += libc.rand() % 2047

    key = data[block_base + offset : block_base + offset + 16]
    offset += 32

    for _ in range(0, 64):
        offset += libc.rand() % 2047
    
    iv = data[block_base + offset : block_base + offset + 16]
    offset += 16

    for _ in range(0, 64):
        offset += libc.rand() % 2047

    offset += 192
    for _ in range(0, 64):
        offset += libc.rand() % 2047

    if(block_base + offset == xor_key_addr):
        break

aes = AES.new(key, AES.MODE_CBC, iv)
print(aes.decrypt(flag_block))
