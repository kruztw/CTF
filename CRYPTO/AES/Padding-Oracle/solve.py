#!/usr/bin/env python3
from pwn import *

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

r = remote("127.0.0.1", 20000)

block_size = 16
enc = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())

def oracle(c):
    r.sendlineafter('cipher = ', c.hex())
    if b'CORRECT' in r.recvline():
        return True
    else:
        return False

flag = b''
for i in range(block_size, len(enc), block_size):
    ans = b''
    pre_block, block = enc[i-block_size:i], enc[i:i+block_size]

    # j : 欲求位置
    for j in range(1, 17): 
        # ch: 窮取所有 char
        for ch in range(256):
            # 計算已知的 intermediate state
            intermediate = xor(pre_block[-j+1:], ans)
            correct_padding = bytes([j]*(j-1))
            
            cipher = pre_block[:16 - j] + bytes([ch]) + xor(intermediate, correct_padding) + block
            if oracle(cipher):
                ans = bytes([pre_block[16 - j] ^ ch ^ j]) + ans
                print(ans)
                break
    flag += ans

print(flag)