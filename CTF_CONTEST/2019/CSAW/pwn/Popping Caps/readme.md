# ctf writeup

難度 :  :star::star:
  

漏洞: <br>
    1. free(ptr + idx); 藉由 idx 可 free 任意位址 <br>
     2. free 後沒設成 NULL <br><br>
    

解題流程: <br>
        直覺來說, 看到 free 後沒 NULL 多半會想到 double free <br>
        而且 bye() 內有 malloc , 因此合理猜測是要我們修改 malloc_hook <br>
        然而這題有限制操作次數 (7 次) <br>
        用 double free 配合 fastbin attack 會超過 <br>
        (add -> free -> free -> add -> write -> add -> add -> write 需要 8 次)<br>
        但要修改 got 或 i 的值都不太可能, 因為 pie 和 aslr 的緣故 <br>
        而且題目已經給 libc 的位址了, 這代表著不需要額外 leak 任何東西 <br>
        那該怎麼辦呢? <br>
        如果我們要直接在 bin 上增加 chunk 就必須改寫 main_arena 或者直接 free 掉要改寫的部份 <br>
        但這些都不可能, 因為 libc 不會無緣無故放一個合法的 chunk header 給你 free <br>
        但那是針對 2.26 以前的版本, 2.27 增加了 tcache ( 它的好處不多說, 絕對是打 heap exploit 的好工具 ) <br>
        tcache 在第一次 malloc 會先 malloc 一塊 0x250 的空間 (含 header) 紀錄相關資訊 <br>
        這些資訊對應到 libc 的 tcache_perthread_struct <br>

```c=
typedef struct tcache_perthread_struct
{
    char counts[TCACHE_MAX_BINS]; // 紀錄各 size 包含的 chunk 數 (共 64 種 size 每種最多含 7 個 chunks)
    tcache_entry *entries[TCACHE_MAX_BINS]; //紀錄指到哪塊 chunk
}

typedef struct tcache_entry
{
    struct tcache_entry *next; // 紀錄指到哪個 chunk 
} tcache_entry;
```
 而在 heap 的結構中, 0x240 前 0x40 個 bytes 紀錄 counts <br>
 剩下的部份為 entries , 用來紀錄第一塊 chunk 的位址<br>
 因此我們只要 free 掉一塊大小為 0x3b0 的  chunk 就能偽造合法的 chunk header, 而且 content 剛好寫到第一個 entries[0] <br>
 剩下的步驟就自行用 gdb trace 了 <br><br>
 
