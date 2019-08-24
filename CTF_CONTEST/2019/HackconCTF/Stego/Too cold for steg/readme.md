難度 :  :star: 
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/Stego/Too%20cold%20for%20steg/pic1.png)

想法 :<br>
        從名字可推出工具為 stegsnow <br>
        但直接 stegsnow -C final.txt 發現是亂碼 <br>
        因此到 final.txt 找線索，搜尋 d4rk 發現 password is ... 這行 <br>
        可見有加密過, 改用 stegsnow -C -p "d4rkc0de-IIITD" final.txt 就能拿到 flag 了 <br>
