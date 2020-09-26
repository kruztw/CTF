#!/usr/bin/env python3
from util import remote

G.<a> = GF(2 ^ 128, modulus=x^128+x^7+x^2+x+1)
R.<x> = PolynomialRing(G)

# bytes to Galois
def b2g(n):
    n = int.from_bytes(n, 'big')
    n = G((Integer(n).bits() + [0] * 128)[:128][::-1])
    return n

# Galois to bytes
def g2b(n):
    n = (Integer(n.integer_representation()).bits() + [0] * 128)[:128]
    n = int(''.join(map(str, n)), 2)
    return n.to_bytes(16, 'big')

def xor(a, b):
    return bytes([x ^^ y for x, y in zip(a, b)])

r = remote('127.0.0.1', 20000)

# 取得兩份 Cipher 和 Tag
r.sendlineafter('user = ', 'AAAAA')
C1 = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())
T1 = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())
r.sendlineafter('user = ', 'BBBBB')
C2 = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())
T2 = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())

L1 = b2g(b'\x00' * 15 + bytes([len(C1) * 8]))
C1 = b2g(C1)
C2 = b2g(C2)
T1 = b2g(T1)
T2 = b2g(T2)

# C 後面還有 L 和 E(J) 所以乘上 x^2 , 詳請請見筆記
# 將 T1 - T2 移到同一邊
f = (C1 - C2) * x ^ 2 - (T1 - T2)
# H 為方程式的根
H, _ = f.roots()[0]
# 代入 H 求 E(J)
EJ = T1 - C1 * H ^ 2 - L1 * H

# bit-Flipping attack
C1_ = xor(g2b(C1)[6:], xor(b'user:AAAAA', b'user:admin'))
C1_ = b2g(C1_)
# 計算新的簽章
T1_ = C1_ * H ^ 2 + L1 * H + EJ

r.sendlineafter('cipher = ', g2b(C1_)[6:].hex())
r.sendlineafter('tag = ', g2b(T1_).hex())
print(r.recvline())
