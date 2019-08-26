難度 :  :star:
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/codefest/Cats%20are%20innocent%20right%3f/pic1.png)

解題流程: <br>
        工具題
```shell=
stegify -op decode -carrier cute_kittens.png -result output
strings ./ouptut
```
