from Crypto.Util.number import long_to_bytes

cipher = '0V]D969E<W1#5$9[-V@Q-5\\Q-5\\T7V,P,#%?,VYC,&0Q;CE]"@'

m = ''
for ch in cipher:
	binary = bin(ord(ch)-32)
	m += str(binary[2:].rjust(6, '0'))

length = ord('E')-32
m = m[:-4]
m = int(m, 2)

print long_to_bytes(m)