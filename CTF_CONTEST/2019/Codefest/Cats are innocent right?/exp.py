from Crypto.Util.number import long_to_bytes

with open('cute_kittens.png', 'rb') as file:
	text = file.read()

lsb_set = ''.join([bin(ord(ch))[-1] for ch in text])

with open('output', 'wb') as file:
	file.write(long_to_bytes(int(lsb_set, 2)))