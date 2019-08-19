想法:<br>
	printf(sanitized); 很明顯的 fsb 漏洞 <br>
	將 exit 的 got 蓋成 winner_room 的位址即可 <br>

解題：<br>
	先用 aaaa%p%p%p... 的技巧發現第 8 個參數可以控到 stack 的位置（也就是說，前 7 個會存暫存器, 其餘的丟 stack ) <br>
	再利用 %{}c%{}$n 寫值 <br>

