IDA 反組譯的結果
```
unsigned int vuln()
{
  char buf; // [esp+Ch] [ebp-8Ch]
  unsigned int v2; // [esp+8Ch] [ebp-Ch]

  v2 = __readgsdword(0x14u);
  memset(&buf, 0, 0x80u);
  system("echo input your message:");
  read(0, &buf, 0x7Fu);
  printf(&buf);
  puts("\n");
  puts("Thanks for sending the message!");
  return __readgsdword(0x14u) ^ v2;
```
```

漏洞:
1. printf(&buf)  存在 format string buffer attack

解題流程:
將 printf 的 got 改寫為 system 的 plt
   puts 的 got 改寫為 vuln 的位址
   
如此一來，當我們再次呼叫到 printf 時，實際上執行的是 system
而 read(0, &buf, 0x7Fu) 可以用來設定 system 的參數 

但要怎麼做呢？
首先，透過 gdb 得到各個 got plt 和 vuln 的位址
接著修改 puts 的 got 為 vuln 的位址 (這樣才能做第二次修改, 另外寫入分兩次較穩定)
等到 printf 執行完，puts 的 got 就變成 vuln 的位址
因此下面呼叫到 puts 時，就會跳回到 vuln 的位址

再次呼叫 vuln 
這次將 printf的 got 修改為 system 的 plt
則當我們第三次回到 vuln 時，printf 已經變成 system 就可以 get shell 了 ( 輸入 sh )


note:
1. payload 會被放到 stack 上，因此 p32(vuln_addr) 在第 7 個參數 (呼叫慣例)
2. 0x10000 用來避免減出來的值是負的 (正的也無妨，反正是 hn)
3. p32 為 32 bytes ，後 16 bits 用 & 0xffff 取得, 前 16 bits 則右移 16 bits
