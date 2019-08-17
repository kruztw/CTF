#!/usr/bin python

from pwn import *

s = ssh(host = '2018shell3.picoCTF.com', user = '')
s.set_working_directory('/problems/keygen-me-1_1_8eb35cc7858ff1d2f55d30e5428f30a7')


param = '999999999999999C'
r = s.process(['./activate', param])

r.interactive()
