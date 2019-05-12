```
解題流程

buf 很大，且沒開 NX , 擺明了是 NOP sled
因為 stk 宣告在 subroutine 而 buf 在 main 
因此，stk 的位址會在 buf 前面
加上 offset 後，可能仍在 buf 前面，也可能在裡面
實際在哪裡，我們不知道
因此，我們能將 ret 加上一個很大的位移，保證該位址在 buffer 裡
接著用 NOP (\x90) 滑到 shellcode 去執行
這方法稱為 nop sled
```
