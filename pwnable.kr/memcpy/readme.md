```

現今的 malloc 大多預設使用 dlmalloc
在 64 位元的電腦以 16byte 為單位 align

因此，輸入 size 時必須要確保下個 malloc 的起始位址為 16 的倍數 (以十六進制表示，即 lsb = 0)
另外，根據 Doug Lea 設計的 chunk 會有 8 byte 額外空間儲存 metadata (prev_size & size)
所以 size = 0x10 實際上要用 0x18 算 (如果是 malloc(0x10) 則會分配 0x20 的空間)

假設輸入的 size 依序為 8    16   32   64    128 ...
則配置的起始位址分別為 0x0  0x10 0x28 0x50  0x98 ...
而在 32 , 128 的起始位址不為 16 的倍數，因此會出錯
但 fast_memory 僅在 len >= 64 時作用
因此會錯在 size = 128 

總結來說，只要確保每次的起始位址皆為 16 的倍數，即可拿到 flag
ex: 
8 24 40 72 136 264 520 1032 2056 4104

```
