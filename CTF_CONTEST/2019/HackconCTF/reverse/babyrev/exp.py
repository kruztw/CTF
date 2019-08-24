import binascii

c = "272d20263a152970741e70741e0233753b383c"
c = binascii.unhexlify(c)

m = ''
for i in c:
	m += chr(ord(i)^0x41)

print m