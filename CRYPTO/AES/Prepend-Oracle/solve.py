#!/usr/bin/env python3
# encoding: utf-8

import string
from pwn import *

r = remote('127.0.0.1', 20000)

# 取得密文
def oracle(m):
    r.sendlineafter('message = ', m.hex())
    return bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())

flag = b''
flag_len = 19
for i in range(flag_len):
    prefix = b'A' * (32 - 1 - i)
    # 先取得正確的 cipher
    target_cipher = oracle(prefix)[:32]

    # 迭代所有可能
    for c in string.printable:
        cipher = oracle(prefix + flag + bytes([ord(c)]))[:32]
        if cipher == target_cipher:
            flag += bytes([ord(c)])
            print(flag)
            break

r.close()
