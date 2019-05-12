```
漏洞
fd=open("/home/mistake/password",O_RDONLY,0400) < 0

< 的優先權較高，所以上面該指令可視為 fd = (open("/home/mistake/password",O_RDONLY,0400) < 0)

如果檔案開啟成功，則 open(...) 回傳 1
又 1 不小於 0 => fd = false = 0

因此 fd 為 stdin

解題流程
password 每一字元會先 xor 1 再跟 pw_buffer 比
因此，讓 pw_buffer = 0000000000 , password = 1111111111
即可得到 flag

```
