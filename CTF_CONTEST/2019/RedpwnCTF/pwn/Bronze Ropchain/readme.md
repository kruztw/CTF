漏洞:<br>
	strcpy(local_1c, param_1); 存在 bof 漏洞 (因為 param_1 可能比較長)

解題流程:<br>
	題目都說 rop 了, 那就 rop 吧 <br>
	x86 rop 拿 shell 方法之一: 利用 execve (eax=0xb, ebx=\*buf(存放 /bin/sh), ecx=0, edx=0) <br>
	要特別注意的是 fgets 遇到 \x00 和 \x0a 就會中斷, 要想辦法避開 <br>
