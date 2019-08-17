```
漏洞

login
45fe:  0f5b           add	r11, r15
4600:  7f90 2100      cmp.b	#0x21, r15

cmp.b 只會檢查一個 byte
因此 0x021 > 0x100

解題流程

輸入 username 長度小於 0x21
接著輸入 password ，且 password 長度與 username 長度相加必須使後面 1 byte 小於 0x21

ex:
username 的長度為 0x20
password 的長度為 0xe0
則兩長度相加為 0x100

透過這樣的方式，我們就能用 password 蓋掉 return address 並將其導到 unlock_door


```
