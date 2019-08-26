難度 :  :star:
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/codefest/Linux%20RE%202/pic1.png)


解題流程: <br>
        跟著走就行了, 我在做時第一步都是先找長度 <br>
        再將已知的字元填入, 最後再一步步滿足它的條件 <br>
        小技巧 : local_73 = return address - 0x73 <br>
        所以 local_74 是上一個字元, local_72 是下一個 <br>