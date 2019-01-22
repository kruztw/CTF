 ```
 漏洞
 1. 檔名為相對路徑 (可繞過一些權限設定, 但此處需用 nc 所以沒用）
 2. strcat 沒做長度檢查
    
解題流程

strcat 會從 name 的終止字元開始蓋
最後再尾端加入新的終止字元


ex
bug.c 是經過精心設計的 bug !?
按照記憶體擺放的順序
password 會在高位址  $rbp-0x20
buffer 會在低位址    $rbp-0x30

當輸入一堆 a 時，$rbp-0x30 ~ $rbp-0x2a 會被塞滿 61 (0x61 => a)
$rbp-0x29 塞入 00 (終止字元）
```

![image](https://github.com/dreamisadream/CTF/blob/master/picoCTF2018/leak-me/leakme1.png)
```
接著 bbbbbbbbb 會從 $rbp-0x29 開始塞
所以 $rbp-0x29 ~ $rbp-0x21 為 62
並在 $rbp-0x20 塞入 00
```
![image](https://github.com/dreamisadream/CTF/blob/master/picoCTF2018/leak-me/leakme2.png)
```
而 $rbp-0x20 正好是 password 起始位址
所以 00  就被 70 (0x70 => p ) 蓋掉了
```
![image](https://github.com/dreamisadream/CTF/blob/master/picoCTF2018/leak-me/leakme3.png)

```
所以輸出就會從 $rbp-0x30 開始往後印，直到終止字元

password 就被 leak 出來了

 
 ```
