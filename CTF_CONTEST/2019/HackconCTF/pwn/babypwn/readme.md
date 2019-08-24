難度 :  :star: 
  
漏洞 :<br>
      1. fgets(&input, 0x11, stdin); (bof) <br>
      2. 沒檢查 index 是否為負數<br>
     
解題流程
     用 gdb 看記憶體發現
     
```c
  input = 0;                      rbp-0x50
  fptr = nope;                 rbp-0x40
  local_38[0] = 0;          rbp-0x30
  local_38[1] = 0;          rbp-0x28
  local_38[2] = 0;          rbp-0x20
  local_38[3] = 0;          rbp-0x18
  local_18 = 0;               rbp-0x10
  i = 5;                              rbp-0x48
```

 input 會蓋到 i 和 fptr 最後一個 byte <br>
原本想說把 fptr 最後一個 byte 蓋成 win 但看到 fgets 就死心了 <br>
因為 fgets 會把最後一個字元的下一個字元寫成 \x00 , 如果填滿的話就把最後一個改成 \x00 因此沒辦法用 <br>
但沒關係，我們還有下一個漏洞 <br>
把 index 寫成負的 (-2) 就能蓋到 fptr 了 <br>
