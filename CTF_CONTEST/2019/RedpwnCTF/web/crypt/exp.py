flag = 'vdDby72W15O2qrnJtqep0cSnsd3HqZzbx7io27C7tZi7lanYx6jPyb2nsczHuMec'
host = 'chall.2019.redpwn.net'
key = ord(host[0]) % ord(host[3])

flag = flag.decode('base64')

m = ''
for i in range(len(flag)):
	m += chr(ord(flag[i])-key)

print m.decode('base64')