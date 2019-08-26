難度 :  :star:
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/codefest/Mailcapture/pic1.png)

解題流程: <br>
      透過文件格式可看出是 [uuencode](https://zh.wikipedia.org/wiki/Uuencode) <br>
      在 linux 直接下 uudecode encoded_flag 就能拿到 flag 了 <br>
      但為了學習我們來手動解一下 <br>
      由 wiki 得知 <編碼內容>  = <長度字元><編碼字元字串> <br>
      因此明文的長度為 ord('E')-32 = 37 = 296 bits<br>
      密文 : 0V]D969E<W1#5$9[-V@Q-5\Q-5\T7V,P,#%?,VYC,&0Q;CE]"@ 共 50 個字元 => 300 bits <br>
      因此我們得知最後有 padding 4 個 0 <br>
      將密文轉成 binary 去掉最後 4 個 0 再轉回 ascii 同樣能拿到 flag <br>
      
