from pwn import *

file = open('./pico2018-special-logo.bmp', 'rb')
info = file.read()

bit = ''
for i in info:
	bit += str(bits(i)[-1])
	
for j in range(8):
	byte = [chr(int(bit[i:i+8], 2)) for i in range(j, len(bit), 8)]
	string = ''.join(byte)

	if 'pico' in string:
		ptr1 = string.find('pico')
		ptr2 = string[ptr1:].find('}')+ptr1+1
		print string[ptr1:ptr2]
		break
