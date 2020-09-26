#!/usr/bin/python3
# encoding: utf-8
from pwn import *

r = process('./server.py')

r.recvuntil('cipher: ')
cipher = r.recvline().strip().decode()
new_c = bytes.fromhex(cipher)

# 明文區塊 1 的位置為 len(prefix)
# 將 IV 的 len(prefix) xor 1
# 明文區塊 1 就會變  {"root": 1 ...
prefix = '{"root": '
new_c = new_c[:len(prefix)] + bytes([new_c[len(prefix)] ^ 1]) + new_c[len(prefix)+1:]
r.sendlineafter('=', new_c.hex())
print(r.recvall())

r.close()