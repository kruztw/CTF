漏洞:<br>
	1. gets 存在 bof<br>
	2. free 沒把指標設成 NULL 可能產生 uaf 漏洞<br>
	3. memcpy(spm->spmm, spm, sizeof(spm)); 可達到任意記憶體寫入<br>

解題流程:<br>
	利用第 3 個漏洞將 got 的內容寫到 chunk (malloc 區塊稱之) <br>
	再利用 writ leak 出 libc 的位址 <br>
	計算出 system 位址後, 將 system 寫入 atoi got <br>
	再利用 writ 輸入 //bin/sh 即可拿到 shell <br> 
