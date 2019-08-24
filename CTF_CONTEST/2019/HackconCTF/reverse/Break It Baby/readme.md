難度 :  :star:
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/reverse/Break%20It%20Baby/pic1.png)

解題流程:<br>
      反組譯後發現 main->test->decrypt 內有 Submit 和 Invalid Password! 因此我們先看這裡 <br>
      要想輸出 Submit 就必須讓 xor 完的結果為 Congratulations <br>
      其中, xor 一邊是已知的，透過和 Congratulations xor 可知另一邊必須是 0x12 <br>
      而這個值是來自於 test 的兩個參數相減 <br>
      一個是輸入值另一個是 0x1673660 <br>
      所以答案就是 0x1673660-0x12 <br>     
