```
漏洞
1. get_rand 的 seed 被當作 cash 使用 (有了 seed 就可以預測數字)
2. get_long 的型態為 long ，但卻回傳 uint64_t 而且 bet 可以是負的

解題流程
將 cash 傳到另一 process 找出 rand 的所有值
接著利用負的 bet 拿到 10億 (別忘了要贏 3 次以上)
```
