利用 IDA pro 反組譯後會發現 </br>
set_timer 將時間設為 1 秒，超過會觸發 Interrupt 執行 alarm_handler 然後 exit(0) </br>
解決方法有 2 個</br>
1. 將 timer 設長點 (利用 gdb)
2. 找出延遲的 function

不難猜出此 function 為 calculate_key </br>
此 function 沒什作為，單純將一個變數從 0x74d2cb96 加到 0xe9a5972c 而且一次只加 1 </br>
然後回傳 0xe9a5972c </br>
因此我們索性用 set 設定就能跳過該函式 </br>

note:
set *<addr> = <value>  (此為 gdb 指令）
