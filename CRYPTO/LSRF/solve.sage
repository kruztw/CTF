#!/usr/bin/env python3
# encoding: utf-8
from sage.matrix.berlekamp_massey import berlekamp_massey

class LFSR:
    def __init__(self, init, feedback):
        self.state = init
        self.feedback = feedback
    @classmethod
    def random(cls, size):
        init = [random.choice([0, 1]) for i in range(size)]
        feedback = [random.choice([0, 1]) for i in range(size)]
        return cls(init, feedback)
    def getbit(self):
        nextbit = reduce(lambda x, y: x ^^ y, [int(i) & int(j) for i, j in zip(self.state, self.feedback)])
        self.state = self.state[1:] + [nextbit]
        return nextbit
    def getbyte(self):
        b = 0
        for i in range(8):
            b = (b << 1) + self.getbit()
        return bytes([b])

def xor(a, b):
    return bytes([i ^^ j for i, j in zip(a, b)]) # ^^ 在 sage 代表 xor , ^ 代表次方

def bytes2bits(x):
    return [int(i) for i in f'{int.from_bytes(x, "big"):0{len(x) * 8}b}']


enc = bytes.fromhex('a9ee8f4d7865376e35')

# 明文 xor 密文 = key (部份 (S0 ~ S31))
stream = xor(enc[:4], b'CTF{')
'''
GF(2)(i) : Galois Field mod 2, 用 i 代入 
e.g. GF(2)(1) = 1, GF(2)(8) = 0
'''
s = [GF(2)(i) for i in bytes2bits(stream)]
assert(len(s) == 32)

'''
berlekamp_massey(s) 獲得 linear recurrence relation 多項式
berlekamp_massey(s).list() 取得係數 (升冪排序)
[0]*16 的目的是為了補齊高次方的係數, [:-1] 是不取最高次的係數 (仔細看筆記會發現多項式最高位係數永遠是 1 且不包含在 linear recurrence relation)
還有就是乘的時候方向是相反的 ai-j * Pj, 所以 [0]*16 放前面代表"後面"的回饋係數等於 0
也許寫成
feedback = berlekamp_massey(s).list()[:-1]
feedback = [0]*(16 - len(feedback)) + feedback 
比較看得懂
'''
feedback = ([0]*16+berlekamp_massey(s).list()[:-1])[-16:]
#print(berlekamp_massey(s))
#print(berlekamp_massey(s).list())
#print(feedback)

# 有 feedback 了就能計算 key 然後 xor 得到明文了
# 注意: feedback 未必跟加密時一樣, 詳情請見筆記
lfsr = LFSR(bytes2bits(stream)[16:], feedback)
key = b''.join([lfsr.getbyte() for _ in range(5)]) # 這個 5 是因為早就知道 flag = CTF{LFSR} 所以取 len(LFSR})
plain = xor(enc[4:], key)
print(b'CTF{' + plain)
