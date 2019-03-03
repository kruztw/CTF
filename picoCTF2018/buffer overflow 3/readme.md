```
漏洞：
1. canary 為定值 且 很短

解題流程:

buffer size 為 32 bytes 超過會被 canary 攔截
一般來說，canary 繞不過的原因是因為他是亂數, 每次執行都不一樣
但這題的 canary 是 user 自行定義，因此為定值
只要一個一個測，就能找出來

有 canary 後，這題就變簡單的 buffer overflow 題
```
