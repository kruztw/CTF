漏洞
1. gets
2. (( void (*)() )buf)(); // buf 可自行輸入

解題流程

找個 shellcode 寫入 buf 就行了
要注意的是，此程式為 32bit，所以要找 x86 的 shellcode

note
(( void (*)() )buf)();

將 buf 轉型為 void (*)() : 不帶參數且回傳 void 的 function

