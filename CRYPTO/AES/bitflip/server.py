#!/usr/bin/python3
# encoding: utf-8

from Crypto.Cipher import AES
import json

flag = b'{"root": 0, "password": "flag{bitflipping_attack}"}'
key = b'very_scret_key!!'
pad_len = 0

def pad(s):
  global pad_len
  pad_len = -len(s)%16
  return s + bytes([0] * pad_len)

def unpad(s):
  return s[:-pad_len]

# m = plaintext
def encrypt(m):
  IV=b"This is an IV456"
  aes = AES.new(key, AES.MODE_CBC, IV)
  return IV.hex()+aes.encrypt(pad(m)).hex()

# m = IV + cipher
def decrypt(m):
  IV=m[:16]
  aes = AES.new(key, AES.MODE_CBC, IV)
  return aes.decrypt(m[16:])


# 傳送 IV + cipher
print(f"Here is a sample cipher: {encrypt(flag)}")

cipher = bytes.fromhex(input('message = ').strip())
message = unpad(decrypt(cipher))
m = json.loads(message)

if m["root"] == 1:
    print(flag.decode())
else:
    print("U are not admin!")