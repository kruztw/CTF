from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long

m = "message"

r = remote('68.183.158.95', 7777)

r.recvuntil('--- ')
r.sendlineafter('Exit\n', '2')
r.sendlineafter(':', '-1')
n = int(r.recvuntil('1)')[1:-2].strip(), 10) + 1

r.sendlineafter('Exit\n', '1')
r.sendlineafter(':', m)
r.recvline()
c = int(r.recvline().strip(), 10)

m = bytes_to_long(m)
for e in range(2**20):
	if pow(m, e ,n) == c:
		print "e = ", e
		break

print "not found"