import re

with open('hello_world.cpp', 'r') as file:
	text = file.readlines()

lines = [''.join(re.findall(r'\s+', line)).replace('\n', '').replace('\t', '1').replace(' ', '0') for line in text]

m = ''
for binary in lines:
	try:
		m += chr(int(binary, 2))
	except:
		pass

print m

