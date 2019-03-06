```
漏洞：
1. free 前未將資料清空 (存在 uaf 漏洞)

解題流程
先索要一塊大小為 0x20 的 chunk
輸入 name 為 '\x05'*9  (由 gdb 看 authority 的位址可知, name 的第 9 個 byte 恰好蓋到其位址)
接著 free 該 chunk
並再次索要相同大小的 chunk
name 隨便輸入，只要不蓋過 authority 的值即可
此時，此帳號之 authority = 5 就能 get-flag 了

note
1. chunk 的大小會隨 name 的長度變化，64位元電腦最小的 chunk 大小為 0x20 

(相關知識)[http://brieflyx.me/2016/heap/glibc-heap/]
