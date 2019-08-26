with open('./image.bmp', 'r') as file:
	text = file.read()

key = 'matrix'
key = (len(text)//len(key))*key + key[:len(text)%len(key)]

with open('./output', 'w') as file:
	for i, j in zip(text, key):
		file.write(chr(ord(i)^ord(j)))