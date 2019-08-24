難度 :  :star: 
  
漏洞 :<br>
      1. printf(&local_28);  (fsb) <br>
      2. fgets(&local_28, 0x100, stdin); (bof) <br>
     
解題流程:<br>
    fsb 的長度只有 0x10 且 got 也不能改, 大概只能用來 leak <br>
    stack 上或暫存器上存有許多有趣的位址 <br>
    隨便拿一個來用就可以 leak 出 libc_base <br>
    (我是拿 stack 上的第 2 個 (%7$p) 它剛好是 stdin 的位址) <br>
    接著利用 bof 跳 one_gadget 結束這回合 <br>
