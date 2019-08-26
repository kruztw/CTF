難度 :  :star::star:
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/codefest/Linux%20RE%201/pic1.png)


解題流程: <br>
        用 strings 看時發現該程式有被加殼 (UPX) <br>
        利用 upx -d 脫殼 <br>
        reverse 後發現, 在 rahasya 輸入的密碼會跟 key_int xor 再回到 main 跟 enc_int 比較 <br>
        因此，把 key_int 和 enc_int 拿出來 xor 就能得到密碼了 <br>
    
