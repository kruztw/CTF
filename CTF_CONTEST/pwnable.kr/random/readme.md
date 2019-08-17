```
漏洞
random() 沒使用 srand  (所以每次的亂數值順序都一樣)

解題流程
在 /tmp (遠端) 寫一個 .c 檔印出 rand()
將亂數值 xor 0xdeadbeef 即為 key 
```
