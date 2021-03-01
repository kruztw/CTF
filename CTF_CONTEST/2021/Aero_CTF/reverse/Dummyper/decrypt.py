#!/usr/bin/env python

from pwn import *

f = open("dump", "rb")
data = f.read()
f.close()

func1_addr = 0x13a9
func2_addr = 0x1691

prologue = asm('''
    endbr64
    push rbp
    mov rbp, rsp
''', arch='amd64')

f1 = data[func1_addr : func1_addr + len(prologue)]
key1 = bytes([x ^ y for x, y in zip(f1, prologue)])

f2 = data[func2_addr : func2_addr + len(prologue)]
key2 = bytes([x ^ y for x, y in zip(f2, prologue)])

key = key1 + key2
key_pos = data.index(key)
key = data[key_pos:key_pos+0x20]
print("key_pos @ ", key_pos)

data = bytearray(data)
for i in range(896):
    data[0x13a9 + i] ^= key[i%len(key)]


f = open("dec_dump", "wb")
f.write(data)
f.close()
