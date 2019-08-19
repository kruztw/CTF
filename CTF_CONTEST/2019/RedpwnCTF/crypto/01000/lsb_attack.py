from pwn import *

hostname = 'chall2.2019.redpwn.net'
port = 5001
s = remote(hostname, port)

def oracle(c1):    
    c1 = str("{0:b}".format(c1))
    print "c1 = ", c1
    s.sendlineafter('>', c1)
    res = s.recvline()
    return int(res)


def partial(c, n):
    lower = 0
    upper = n
    while True:
        c = (c * pow(2, e, n)) % n 
        lsb = oracle(c)
        if not lsb:
            upper = (lower + upper) / 2
        else:
            lower = (lower + upper) / 2
        print "upper - lower = ", int(upper - lower)
        print "upper = ", hex(int(upper))


if __name__ == '__main__':
    s.recvuntil(': (')
    info = s.recvuntil(')')[:-1].split(',')
    n, e = int(info[0], 2), int(info[1], 2)
    s.recvuntil(': ')
    c = int(s.recvline(), 2)
    print "n = ", n
    print "e = ", e
    print "c = ", c
    partial(c, n)
    s.interactive()