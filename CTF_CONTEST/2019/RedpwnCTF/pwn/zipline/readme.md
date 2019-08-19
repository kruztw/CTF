漏洞:<br>
	gets 存在 bof <br>

解題流程:<br>
	這題有很多種解法，可以拿到 shell 也可以只讀 flag <br>
	感覺拿到 shell 的很常見, 所以就簡單寫個只讀 flag  的 <br>
	要讀取 flag 就是跳到 i_got_u 的 open 上面就行了<br>
	但該位址有個討厭的 \x0a (會中斷 gets 讀取) <br>
	因此我們從 main 進去 <br>
	但從 main 進去要繞過它的限制, 也就是變數 a ~ h 都不能等於 0 <br>
	幸運的是 a ~ h 都在 bss 段，所以我們可以利用 gets 將該段寫入任意值 <br>
	但要小心別蓋到 got 否則會出錯 <bz>
