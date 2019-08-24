難度 :  :star: 
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/Stego/Small%20icon%20much%20wow/pic1.png)

想法 :<br>
        用 binwalk 發現藏有圖片 <br>
        使用 dd if=stego.jpg of=output skip=202 bs=1 將圖片萃取出來 <br>
        打開圖片後發現是 QR code <br>
        利用網路工具 [QR decode](https://zxing.org/w/decode.jspx) 就能拿到 flag 了 <br>
