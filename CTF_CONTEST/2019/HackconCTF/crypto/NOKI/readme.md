  難度 :  :star: 
  
  ![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/crypto/NOKI/pic1.png)

解題想法 : <br>
	題目說明加密方式為 Vigenère Cipher <br>
    因此我們找到常用的[加密表](https://zh.wikipedia.org/wiki/%E7%BB%B4%E5%90%89%E5%B0%BC%E4%BA%9A%E5%AF%86%E7%A0%81#/media/File:Vigen%C3%A8re_square.svg) <br>
    並查找 giu 和 drk (g4iu == d4rk) <br>
    發現  DD 對到 g , RR 對到 i , UU 對到 k <br>
    透過這個原則我們可以將每一個密文對到兩個字元 <br>
    再自己推敲該選哪個 <br>
    