from Crypto.Util.number import *

m = '505d034303560b6e40025a1b541c6e4b034534060b0550585a58'.decode('hex')

key = '1337key'
key = (len(m)//len(key))*key + key[:len(m)%len(key)]

ans = ''
for i, j in zip(m, key):
	ans += chr(ord(i)^ord(j))

print ans