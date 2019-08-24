from Crypto.Util.number import long_to_bytes

with open('./file', 'r') as f:
	text = f.read().replace('\\n', '').replace(' ', '')

output = open('./output', 'wb')
output.write(long_to_bytes(int(text, 16)))
output.close()
