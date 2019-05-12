from pwn import *

greeting_message = "You have now entered the Duck Web, and you're in for a honkin' good time.\nCan you figure out my trick?"
key = "\x29\x06\x16\x4F\x2B\x35\x30\x1E\x51\x1B\x5B\x14\x4B\x08\x5D\x2B\x50\x14\x5D\x00\x19\x17\x59\x52\x5D\x00"

s = ""
for i in range(25):
    s += chr(ord(key[i]) ^ ord(greeting_message[i]))

print s

