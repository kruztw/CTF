難度 :  :star::star:
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/reverse/babyrev/pic1.png)

解題流程:<br>
      用 ghidra 打開後發現 main 只讀取 user 然後就離開了<br>
      根據我打 pwn 的經驗, check 一定出現在 .fini_array <br>
      果不其然, .fini_array 有兩個函式, 一個是 check 另一個是 end <br>
      由於 .fini_array 執行順序是由後往前，所以是先執行 end 再執行 check <br>
      在 end 裡可以看到 result , 而 check 就是用 result == 0 來決定輸出 <br>
      因此我們的目標就是讓 result = 0 <br>
      而 result 是由 ruser 和 pass 和 0x41  xor 來的 <br>
      因此可以得知 ruser = pass xor 0x41 <br>
      pass 用 gdb 就可以取得, 而 user 和 ruser 差 0x10 <br>
      因此輸入 user = aaaaaaaaaaaaaaaaflag{Th15_15_Cr4zy} 就過關了 <br>
      
