asm.c

sh 指到 mmap 一段大小為 0x1000 的區域 ( [mmap 詳細介紹](http://welkinchen.pixnet.net/blog/post/41312211-%E8%A8%98%E6%86%B6%E9%AB%94%E6%98%A0%E5%B0%84%E5%87%BD%E6%95%B8-mmap-%E7%9A%84%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95))</br>
前面放 stub (用 pwntool 的 disasm 可以看出這段程式只是在初始化暫存器)</br>
後面放使用者輸入的 code (長度上限為 1000)</br>
接著將根目錄改到 /home/asm_pwn  (想當然而是我們 cd 進不去的位置)</br>
並開啟 sandbox<br>
sandbox 限制我們只能使用 open read write exit exit_group 的 system call ( [seccomp 介紹](https://veritas501.space/2018/05/05/seccomp%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/))</br>
最後執行 sh </br>


因此，我們的想法是利用 open 開啟存放 flag 的檔案</br>
再用 read 將 flag 讀到 stack 上 (也就是 rsp 指到的位址)</br>
最後再用 write 將 flag 寫到 stdout (fd = 0) </br>


[x86_64 system call](https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/)


