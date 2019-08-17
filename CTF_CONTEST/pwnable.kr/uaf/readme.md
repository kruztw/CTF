```
漏洞：
1. delete m 和 w 之後，沒有將 m 和 w 設成 nullptr

解題流程：

將 m 、w delete 後，再 allocate 相同大小的 chunk
則系統會將剛剛 delte 掉的 chunk return 給你
接著寫入 give_shell - 0x8 的位址
再呼叫 m->introduce ，就能 getshell 了

python -c "print '\x68\x15\x40\x00\x00\x00\x00\x00'" > /tmp/key
./uaf 24 /tmp/key

note:
1. 為什麼 allocate 相同大小的 chunk 會 return m 那塊 ?
這是因為 m 的大小符合 fastbin ，而 fastbin 是 LIFO (剩下的請自行 google)
這也是為什麼要 allocate (after) 二次，因為是先 delete m 再 delete w
而 use 是先 m->introduce 再 w->introduce

2. 為什麼大小是 24
用 gdb 可以看出來 new 前面分配 0x18 的大小

3. 為什麼是 give_shell - 0x8，為什麼將這個值寫入 m 有用 ?
首先，class 內如果有使用 virtual function
則編譯時會建立一個 vtable 和一個 vptr
vtable 紀錄 virtual function 的位址 (按宣告順序依序紀錄在 vtable + 0x10, vtable + 0x18, ... )
vptr 指向 vtable
因為 human 有 virtual function
所以 human 有 vtable
又因為 man ( woman 也是 ) 繼承 human
所以 man 會複製 human 的 vtable (ps: 當有 virtual function overloading 時，會直接修改 vtable 的位址)

在宣告的時候
man *m = new man;
m 的值會指向 vtable 中第一個 virtual function 的位址 (也就是 give_shell)
由於 introduction 是第二個 virtual function
因此 m->introduction 相當於是呼叫 m+0x8 的位址
所以，如果我們將 m 的值修改為 give_shell - 0x8 
那麼 m->introduction 就會呼叫 give_shell

```
