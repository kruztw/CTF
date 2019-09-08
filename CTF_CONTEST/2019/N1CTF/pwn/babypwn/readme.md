難度 :  :star::star::star:
  

漏洞: <br>
    1. free 後沒清成 NULL 存在 double free <br>
    2. idx 可以是負的 (out of bound) <br><br>
    

解題流程: <br>
    這題給我的感覺就是跟 warmup 差不多, 整體流程不外乎修改 file structure 和 malloc_hook <br>
    所以完全沒用到漏洞二 <br>
    但這題是執行在 libc-2.23.so 的環境, 所以沒有 tcache <br>
    但這不是什麼大問題, 因為 fastbin 只會檢查第一個 chunk 的位址和要 free 的是否相同<br>
    因此 free(0) free(1) free(0) 就能繞過了 <br>
    另外就是, 它有限制最大 member 數不能超過 10 個 (別忘了 free 沒設成 null)<br>
    用膝蓋想就知道這不可能, 光 fastbin attack 要拿到 fake chunk 就用 6 個了 <br>
    (add(0) add(1) free(0) free(1) free(0) add(0 修改) add(1) add(0) add(fake)) <br>
    因此必須得拿到存放 member 的 chunk 將他們清空 (好在沒開 PIE) <br>
    剩下的就是考驗腦袋的結構是否能邊 exploit 邊思考 heap 的情況惹 <br>
    喔, 對了, 因為每次新增 member 都會多 malloc(0x20) 存放 meta data <br>
    所以要盡量避免使用到 0x30 的 chunk 否則會被拿走 <br>
    而且一開始前面 3 塊的大小和 free 順序都有精心設計過<br>
    這樣才能讓 fd 和欲得到的位址在同一個 page (講白話就是只差最後一個 byte), 否則得寫入兩 bytes, 那就得猜了(因為 aslr) <br><br>
    
    

後記<br>
    這題真的要抱怨一下, 題目沒給 libc.so.6 且前一題的環境是 libc-2.27.so <br>
    因此合理猜測這題應該也是 2.27 結果竟然是 2.23 兩個版本差了個 tcache <br>
    結果就是兩個版本的 exploit 都寫出來了@@ (但沒拿到 bonus  (前三殺))<br>
    