漏洞 : <br>
	簡易版的 blind fsb 漏洞 <br>

解題流程 :<br>
	之所以說簡易版，是因為它沒有開 PIE 所以 got table 位址固定 <br>
	怎麼知道沒開呢 ? <br>
	因為 fsb 的格式通常是 scanf / read / fgets 伴隨 printf(buf) <br>
	printf 只會用到 rdi , 而 scanf / read /fgets 都會用到二個以上的變數 <br>
	因此 rsi rdx 會透漏些資訊 <br>
	可利用 %1$p %2$p leak 出來 <br>
	之後便依照輸出位址判斷是否有開 PIE 也可以判定它是 32位元還 64位元<br>
	如果沒開 PIE，則 got 的位址通常會放在 0x0804_000 (32位元) 的地方 ( \_可能是 a 或 b 等等) <br>
	但即便有開，也可以在 leak 出某位址時猜測 pie base <br>
	對於複雜的題目可能得先 leak 出部份 ELF (可利用 leak.py) 再加以分析<br>
	相對簡單的可以直接試著修改 got (exp.py) <br>
	但要怎麼知道哪個 got 對到哪個呢 ? <br>
	很簡單，每個都試就知道了 <br>
	我在 leak 時順便計算 read 和 fgets 發現把 0x0804a010 當作 printf got 時, 出現與 fgets 相同位址的 got 值 <br>
	因此便能確定 printf 的 got 位址，剩下的就是改成 system 即可 <br>

