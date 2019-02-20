def decrypt(ch):
	ch = int(ch, 16) ^ 0x16
	ch = (ch<<4 | ch>>4)%(2**8)
	return chr(ch)


cipher = '11 80 20 E0 22 53 72 A1 01 41 55 20 A0 C0 25 E3 45 20 35 05 70 20 95 50 C1'
message = map(decrypt, cipher.split(' '))

print ''.join(message)
