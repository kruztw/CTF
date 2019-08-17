漏洞： </br>

brainfuck 可任意位址寫入與讀取 </br>

流程: </br>

將 puts 寫入返回位址，並將 memset 的 got 改成 gets，fgets 的 got 改成 system </br>
則當下次寫入時輸入 /bin/sh 即可執行 system("/bin/sh") </br>
