#! /usr/bin/python3

file = open('./encrypted.txt')
cipher = file.read()
file.close()

block_cipher = [cipher[i::38] for i in range(0, 38)]

key = ''
for c in block_cipher:
	key += chr(max(list(map(ord, c))) ^ ord('։'))

print(key)