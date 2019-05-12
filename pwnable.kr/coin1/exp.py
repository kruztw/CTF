from pwn import *

r = remote('pwnable.kr', 9007)


r.recvuntil('... -\n')
r.recvline()

for _ in range(100):

	info = r.recvline().split()
	N, C = int(info[0][2:]), int(info[1][2:])

	left, right = 0, N
	middle = (left+right)//2

	for _ in range(C):
		
		r.sendline(' '.join([ str(i) +' ' for i in range(left, middle+1)]))

		if int(r.recvline()) % 2 == 1:
			right = middle
		else:
			left = middle + 1

		middle = (left+right)//2

	r.sendline(str(middle))
	print(r.recvline())

r.interactive()
