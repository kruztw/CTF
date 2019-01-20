漏洞：

strcpy 不會檢查 copy 的字串長度是否超過 buffer

note: 應用 strncpy

解題流程：

signal(SIGSEGV, sigsegv_handler);
當接獲到 signal 且原因為 SIGSEGV 時，自動執行 sigsegv_handler
SIGSEGV 發生的原因： 非法存取 disk 或 memory

因此，只要將 argv[1] 輸入一大堆文字導致 overflow 就會觸發 SIGSEGV
從而執行 sigsegv_handler

sigsegv_handler 會將 flag 導到 stderr 

google 一下 stderr 和 stdout 的差別
stderr: Procedure output to the console Used in C with printf
stdout: Procedure output to the console Used in C with fprintf

所以最終都會顯示在螢幕上

