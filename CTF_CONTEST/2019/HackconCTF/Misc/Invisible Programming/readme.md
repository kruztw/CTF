難度 :  :star:
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/Misc/Weird%20Text/pic1.png)

解題流程:
      用 sublime 打開後發現排版很奇怪, 且按下 ctrl + A 後發現有 \t 和 ' '<br>
      這通常有幾種可能 <br>
      1. 1 和 0
      2. morse code
      我首先猜 morse code 因為 sublime 的 \t 用 - , 空格用 . 表示 <br>
     但怎麼試都不對, 因此改用 1 和 0 <br>
     每一行代表一個字 <br>
     最後出來的結果有些奇怪, 但勉強能猜出 flag <br>