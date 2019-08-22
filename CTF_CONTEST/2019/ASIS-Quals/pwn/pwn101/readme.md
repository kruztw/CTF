  難度 :  :star: :star:  
  
  漏洞:

  - add 時, description 可多輸入一個字元 ( Overlapping chunk )<br>
       
           
   ---
  
  解題流程:
           
 * 概略 <br>
          修改 chunk size 產生 Overlapping chunk
          再 leak 該 chunk 拿到 libc_base
          最後再用 fast bin attack 修改 free hook 成 system
          delete 掉含 system 的 chunk 
 
