  難度 :  :star: :star:
  
  漏洞:

  - 沒檢查輸入的個數是否超過陣列最大值 ( bof ) <br>
       
           
   ---
  
  解題流程:
           
 * 概略 <br>
         因為有開 NX 所以方向選定 ROP<br>
          首先先用 puts_plt 洩漏 libc_base 並跳回 main <br>
          再一次 bof 跳到 one_gadget 就拿到 shell 了<br>

* 難點 <br>
    * 輸入格式為 double  : <br>
         "%.800f " % unpack("<d", p64(data))
    
    * bypass canary :<br>
    輸入 - 可繞過 (scanf 數字 : 輸入 - 會保留原本的值)
