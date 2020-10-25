#!/usr/bin/env python2
# from Hack.lu CTF 2020 Bad Primes

import binascii
from Crypto.Util.number import *


# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


n = 3283820208958447696987943374117448908009765357285654693385347327161990683145362435055078968569512096812028089118865534433123727617331619214412173257331161
p = 34387544593670505224894952205499074005031928791959611454481093888481277920639
q = 95494466027181231798633086231116363926111790946014452380632032637864163116199
e = 65537


# flag = "flag{...}"
# flag = int(binascii.hexlify(flag), 16)
# flag = pow(flag, e, n)
d = modinv(e, (p - 1) * (q - 1))

d = 1
while 1:
    flag = 2152534604028570372634288477962037445130495144236447333908131330331177601915631781056255815304219841064038378099612028528380520661613873180982330559507116
    d += 1
    if d == None:
        print("definitely too primitive...")
    else:
        print("d = ", d)
        try:
            flag = pow(flag, d, n)
            flag = hex(flag)[2:]
            flag = binascii.unhexlify(flag)
            if "{" in flag:
                print("d = ", d)
                break
        except:
            pass

