import hashlib
import string

char_set = string.printable


target = 'CD04302CBBD2E0EB259F53FAC7C57EE2'

key = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

while True:
	m = ''
	for i in range(len(key)):
		if key[i] != -1:
			m += char_set[key[i]]

	c = m
	for _ in range(10):
		md5 = hashlib.md5()
		md5.update(c)
		c = md5.hexdigest().upper()

	if c == target:
		print m
		break

	key[-1] += 1
	for i in range(len(key)-1, 0, -1):
		if key[i] == len(char_set):
			key[i] = 0
			key[i-1] += 1
		else:
			break