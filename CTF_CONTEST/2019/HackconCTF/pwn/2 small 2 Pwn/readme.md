難度 :  :star: 
  
漏洞 :<br>
      1. read 有 0xa0 的空間, 用 gdb 測試發現存在 bof 漏洞
     
解題流程 :<br>
    沒開任何保護, 那就 return to shellcode  ( 把 shellcode 放到 bss 再跳過去執行 )<br>
    另外, 因為本地端 r.sendline 沒反應, 遠端可以, 因此加上 stdin=PTY <br>
    詳細情形還不太清楚 <br>
