from pwn import *

r = remote('2018shell3.picoctf.com', 1225)

Q1 = r.recvuntil(':\n').split('\n')[2].split(' ')

A1 = ''
for i in Q1:
    if i.isdigit():
        A1 += chr(int(i, 2))

r.sendline(A1)


Q2 = r.recvuntil(':\n').split('\n')[0].split(' ')
A2 = ''

for i in Q2:
    if i[0].isdigit(): 
        A2 = i.decode('hex')
        break

r.sendline(A2)


Q3 = r.recvuntil(':\n').split('\n')[0].split(' ')
A3 = ''
for i in Q3:
    if i.isdigit():
        A3 += chr(int(i, 8))

r.sendline(A3)


flag = r.recvall().split('\n')[1]
print flag


