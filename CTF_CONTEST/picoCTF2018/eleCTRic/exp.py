#!/usr/bin python

from pwn import *

def xor(str1, str2):
	s = ''
	for a, b in zip(str1, str2):
		s += chr(ord(a) ^ ord(b))
	return s

r = remote("2018shell3.picoctf.com", 36150)

r.recvuntil("choose:")
r.sendline("i")

flag_name = r.recvuntil('choose:').split('\n')[2][2:] # plaintext2

fileName = 'aaaaaaaaaaaaaaaaaaaaaaaaa' #plaintext1 = aa...a.txt
r.sendline('n')
r.sendline(fileName)
r.sendline('a') #garbage

share_code = r.recvuntil('choose:').split('\n')[2]  # base64(cipher1)
shareDecode64 = share_code.decode('base64') # cipher1

#cipher = plaintext xor function

function = xor("{}.txt".format(fileName), shareDecode64)  # function = cipher1 xor plaintext1
cipher2 = xor(flag_name, function) # cipher2 = plaintext2 xor function

r.sendline('e')
r.recvuntil("code? ")
r.sendline(cipher2.encode('base64')) # cipher2.encode('base64') = share code

print r.recvuntil('}')
r.close()
