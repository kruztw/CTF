from pwn import *
import binascii

def chineseRemainderTheore(am, b):
	if b == 0:
		return (a, 1, 0)

	(gcd, coef1, coef2) = chineseRemainderTheorem(b, a%b)

	tmp = coef1
	coef1 = coef2
	coef2 = tmp-(a/b)*coef2

	return (gcd, coef1, coef2)


r = remote('2018shell3.picoctf.com', 50430)

info = r.recvuntil('(Y/N):')
pPos = info.find('p : ')
qPos = info.find('q : ')
p = info[pPos+4:].split('\n')[0]
q = info[qPos+4:].split('\n')[0]

r.sendline('Y')
r.sendline(str(int(p, 10)*int(q, 10)))


info = r.recvuntil('(Y/N):')
pPos = info.find('p : ')
nPos = info.find('n : ')
p = info[pPos+4:].split('\n')[0]
n = info[nPos+4:].split('\n')[0]

r.sendline('Y')
r.sendline(str(int(n, 10)//int(p, 10)))


info = r.recvuntil('(Y/N):')
r.sendline('N')

info = r.recvuntil('(Y/N):')
pPos = info.find('p : ')
qPos = info.find('q : ')
p = info[pPos+4:].split('\n')[0]
q = info[qPos+4:].split('\n')[0]

r.sendline('Y')
r.sendline(str( (int(p, 10)-1)*(int(q, 10)-1) ))


info = r.recvuntil('(Y/N):')

tPos = info.find('t : ')
ePos = info.find('e : ')
nPos = info.find('n : ')
t = info[tPos+4:].split('\n')[0]
e = info[ePos+4:].split('\n')[0]
n = info[nPos+4:].split('\n')[0]

r.sendline('Y')
r.sendline(str(int(t, 10)**int(e, 10)%int(n, 10)))

info = r.recvuntil('(Y/N):')
r.sendline('N')


info = r.recvuntil('(Y/N):')

pPos = info.find('p : ')
qPos = info.find('q : ')
ePos = info.find('e : ')
p = info[pPos+4:].split('\n')[0]
q = info[qPos+4:].split('\n')[0]
e = info[ePos+4:].split('\n')[0]

p = int(p, 10)
q = int(q, 10)
e = int(e, 10)

(gcd, d, coef_phi) = chineseRemainderTheorem(e, (q - 1) * (p - 1))

r.sendline('Y')
r.sendline(str(d))


info = r.recvuntil('(Y/N):')

pPos = info.find('p : ')
tPos = info.find('t : ')
ePos = info.find('e : ')
nPos = info.find('n : ')
p = int(info[pPos+4:].split('\n')[0], 10)
t = int(info[tPos+4:].split('\n')[0], 10)
e = int(info[ePos+4:].split('\n')[0], 10)
n = int(info[nPos+4:].split('\n')[0], 10)

q = n//p
phi = (p-1)*(q-1)
(gcd, d, coef_phi) = chineseRemainderTheorem(e, phi)

while d < 0: d+=phi
r.sendline('Y')
r.sendline(str(pow(t,d,n)))


m = hex(pow(t,d,n))[2:]
print 'flag: ', binascii.unhexlify(m)
