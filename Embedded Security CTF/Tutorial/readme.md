```
check_password 會將 r15 指到的值 assign 給 r14  (mov.b @r15, r14)
接著將 r12 加 1       (inc r12)
如果 r14 不等於 0 則回到 check_password (tst r14; jnz #0x4484 <check_password+0x0>)

很顯然 r12 為輸入的長度

如果 r12 = 9 則將 r15 寫入 1 ，就破關了

=> answer: aaaaaaaaaaaaaaaa ( aa 為 1 byte)

因為是先加 r12 再檢驗 r14
所以密碼長度須為 8 
```
