難度 :  :star: :star::star:
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/Stego/GIMP%20IT/pic1.png)

解題流程:<br>
    用 gimp 打開發現 Nothing here layer 但似乎沒什麼用 <br>
    改用 strings 看它, 發現 (text: "504b 0304 ...") 這是 zip 的 header <br>
    將這段貼到 file 再用 convert.py 輸出到 output 再 unzip 可得 data.txt <br>
    將 data.txt 用 draw.txt 轉成 QR code 再用 zbarimg 掃描即可拿到 flag <br>

