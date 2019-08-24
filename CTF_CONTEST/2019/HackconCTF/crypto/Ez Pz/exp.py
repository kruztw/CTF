from pwn import *
from Crypto.Util.number import long_to_bytes

e = 65537

r = remote('68.183.158.95', 7777)

r.recvuntil('--- ')
c = int(r.recvline().strip(), 10)

r.sendlineafter('Exit\n', '2')
r.sendlineafter(':', '-1')
n = int(r.recvuntil('1)')[1:-2].strip(), 10) + 1

r.sendlineafter('Exit\n', '2')
r.sendlineafter(':', str(c*pow(2, e, n)%n) )
r.recvline()

m = int(r.recvline().strip(), 10)
print long_to_bytes(m/2)

