```
漏洞
1. gets 存在 bof
2. flag.txt 為相對路徑

解題流程

透過 gets 可控制 eip
首先，跳到 win_function1 讓 win1 變成 true
接著，跳到 win_function2 並將參數設為 0xBAAAAAAD (參數位址為 ebp + 0x8 而 ebp = esp 所以放在 p32(win2_addr) 後兩個即可)
最後，跳到 flag 並將參數設為0xDEADBAAD 即可得到 flag


note

ebp = esp 是因為 win_function2 的 prelogue 有 mov ebp, esp
另外，當跳到 win_function2 時，代表 esp 在 p32(win2_addr) 後了
```
