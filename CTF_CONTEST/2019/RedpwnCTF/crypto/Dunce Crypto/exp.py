cipher = 'mshn{P_k0ua_d4ua_a0_w4f_tf_ahe3z}'

offset = ord(cipher[0]) - ord('f')

m = ''
for i in cipher:
	if i.isalpha():
		if i.islower():
			m += chr((ord(i) - ord('a') - offset + 26)%26 + ord('a'))
		else:
			m += chr((ord(i) - ord('A') - offset + 26)%26 + ord('A'))


	else:
		m += i

print m