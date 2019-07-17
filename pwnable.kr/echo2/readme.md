漏洞: <br>

    1. printf(buf) 存在 fsb 漏洞

    2. exit 先 free(fptr) 才判別是否離開，這會導致 uaf 拿到該 chunk

解題流程: <br>

方法一：<br>

	利用 fsb 將 fgets 改成 gets，再觸發 bof (此時就回到 echo1 了)<br>

note:<br>
1. libc.so.6 需用 pwnable.kr 的，否則版本不同，偏移量也會不同
2. 因為 fgets 跟 gets 的偏移量很接近，因此只要改末 2 bytes 即可

詳情請見 exp1.py<br>


<br>
<br>
方法二: <br>

	先用 fsb leak 出 name 的位址，此時得自行觀察 stack 上是否有與 name 位址偏移量固定的值<br>
	再利用 uaf 漏洞改寫 fptr ( echo2 用 o 表示 ) 的 chunk ， 將 greetings (fptr[3])  改為  name ，name 的內容為 shellcode<br>

詳情請見 exp2.py
	
