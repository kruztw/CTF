```
執行 ./flag 出現以下資訊
I will malloc() and strcpy the flag there. take it.

因此我先使用 strings 看看是否能找出 flag
結果發現
This file is packed with the UPX executable packer http://upx.sf.net

其實反編譯後會發現程式短到不行，就有點 UPX 的味道了
透過 upx -d ./flag 將 flag 脫殼
接著再用 strings 找找看
strings ./flag | grep -i upx  ( upx 是猜的 )
因此可得 flag
UPX...? sounds like a delivery service :)

如果沒有，也可用 gdb 去看 flag 的內容
```
