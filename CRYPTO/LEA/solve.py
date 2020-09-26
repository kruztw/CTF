#!/usr/bin/env python3
#encoding: utf-8

import hashpumpy
from base64 import b64encode, b64decode
from pwn import *

r = remote('127.0.0.1', 20000)

r.recvuntil('your token: ')
token = b64decode(r.recvline().strip())
r.recvuntil('your authentication code: ')
auth = r.recvline().strip()

IV = auth
origin_data = token
new_data = 'user=root'
salt_len = 12
new_auth, new_token = hashpumpy.hashpump(IV, origin_data, new_data, salt_len)
r.sendlineafter("input your token: ", b64encode(new_token))
r.sendlineafter("input your authentication code: ", new_auth)
#print("new_token = ", new_token) # 從 user=kruztw 到 user=root
#print("new_auth = ", new_auth) # 大塊 hash 值

print(r.recvline().decode())