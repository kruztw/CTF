from pwn import *

s = ssh(host='2018shell3.picoCTF.com', user='kruzXavier')

s.set_working_directory('/problems/in-out-error_4_c51f68457d8543c835331292b7f332d2')
s.run('echo "Please may I have the flag?" | ./in-out-error 2>/tmp/flag')
flag = s.run('cat /tmp/flag').recvall().split('}')

print flag[0],'}'

s.close()


