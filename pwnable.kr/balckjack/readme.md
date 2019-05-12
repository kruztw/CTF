```
漏洞
1. bet 可以小於 0
2. bet 可以超過 cash (只有第一次會被擋下來 )

問題
1. main 的 choice1 沒有用
2. printf("%c", spade); 型態不符
3. asktitle 呼叫 rule，rule 再呼叫 asktitle 可能灌暴記憶體
4. 1 有可能被印出來, 10 永遠不會出現
5. Ace 可能為 1 或 11 
6. clubcard() randcard() betting() 回傳 global variable ??? (需要嗎?)
7. 不列了


```
