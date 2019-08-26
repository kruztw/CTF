難度 :  :star:
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/codefest/Weird%20encoding/pic1.png)



解題流程: <br>
    用 bless 或 hexeditor 打開後發現一串數學式 <br>
    但那不是數學, 那是一張圖 <br>
    0 表白色, 1 表 黑色 , 0x85 代表有 85 個白色 <br>
    將圖畫出來, 即可得到 flag <br>