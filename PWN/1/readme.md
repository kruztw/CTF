漏洞:</br>

printf(buf) 存在 fsb</br>

解題流程:</br>

將 puts_got 改寫為 read(0, buf, 0x100) 的位址 </br>
同時將 printf_got 改寫為 system_plt </br>

則執行到 puts 會跳回 read </br>
輸入 /bin/sh 即能在 printf(buf) 拿到 shell </br>


note: </br>
ln 大小為 8bytes</br>
透過 %1c%10$ln 可將 got 的內容改成 0x01</br>




