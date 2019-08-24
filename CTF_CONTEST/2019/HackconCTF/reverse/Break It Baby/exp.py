c = "Q}|u`sfg~sf{}|a3"
key = "Congratulations!"


m = ''
for i, j in zip(c, key):
	m += str(ord(i) ^ ord(j))

print m # 18 = 0x12

ctx = 0x01673660 - 0x12
print ctx