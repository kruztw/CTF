難度 :  :star::star:
  

漏洞: <br>
    1. free 後沒清成 null <br>


解題流程: <br>
        在 name 創一個大小為 0x420 的 chunk, 並將其 free <br>
        此時, unsorted_bin + 0x60 的位址會被寫在 name 裡 <br>
        print name 計算 one_shot 的位址, 並填入 malloc_hook <br>
        再 malloc 就能拿到 shell 了  <br>

note: <br>
    1. 大小超過 0x420 的 chunk 不會放到  tcache, 而是直接放到 unsorted bin <br>
    2. 0x3ebc40 為 unsorted bin 到 libc_base 的距離 <br>
    3. free_hook 會比 malloc_hook 好做, 因為 malloc_hook 要繞過 movaps, 方法是用 realloc hook (詳情見 exp.py) <br>