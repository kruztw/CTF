```
將 ./main 反組譯後可發現字串加密方式為

rol4 : 將字元左旋 4 bits
ror8 : 將字元右旋 8 bits

順序為 rol4 -> xor 0x16 -> ror8

因此，只要將密文反著做就能拿到 flag 了


note:

1. 
rax : 64 bits
eax : 32 bits
 ax : 16 bits
 al :  8 bits
 ah :  8 bits
 
2.
al = 0x41 左旋 4 bit -> 0x14
因為
al 為 8 bits，轉成 2 進制為 01000001 
所以左旋 4 bits -> 00010100 = 0x14

因此，對於 al (8 bits) 來說，ror8 是沒意義的
```
