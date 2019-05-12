from pwn import *
import string

flag = ''
alphabet = string.printable.replace("'", '')

for i in range(43):

	for ch in alphabet:
		payload = 'a'*(43-i) + 'fying code is: ' + flag + ch + 'a'*(48-i)
		print payload
		r = remote('2018shell3.picoctf.com', 30399)
		r.sendline(payload)
		r.recvuntil(': ')
		info = r.recvall()
		if info[192:223] == info[352:383]:
			flag += ch
			print 'flag = {}'.format(flag)
			break

	if flag[-1] == '}':
		break
