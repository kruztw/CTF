透過 IDA-pro 可知, key 的計算方式
由於該程式是用遞迴計算
因此速度極慢
將該函式寫成 iterative 形式
很容易可以算出 key 為 2653079950
再用 gdb 的 set 就能印出 flag 了
