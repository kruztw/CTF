# ctf writeup

難度 :  :star::star::star:
  

漏洞: <br>
1. login 後的第五個操作(修改 address 存在型態不一致問題)scanf 是 %d 但 edit_addr 卻是 uint<br>

    
解題流程: <br>
輸入 -1 就能 heap overflow 了, 剩下的應該沒什麼難的<br>

心得:
這題難在 reverse 啦, 其實超簡單的 <br>
但解的人數比 dusty_box 還少, 可能是因為 dusty_box 很難, 而這題出在它後面ㄅ <br>