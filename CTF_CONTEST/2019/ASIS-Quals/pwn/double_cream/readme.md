  難度 :  :star: :star: :star:
  
  漏洞:

  - printf(&DAT_00301060); ( fsb )<br>
       
           
   ---
  
  解題流程:
           
 * 概略 <br>
            隔了兩個 function 才觸發 fsb , 直接猜 rbp chain <br>
            但這題不能改 got 所以我們只能改 return address <br>
            但 ra 在 stack 上只能用猜的 (機率 $1\over16$) <br>
            因此整體流程共分兩步 <br>
            第一次進到 foo2 修改 foo1  的 rbp 指到 foo1 的  return 位址 , 並修改為 call foo2 的位址 <br>
            順便 leak __libc_start_main 的位址然後將 foo1 的 rbp 指到 main 的 return 位址 <br>
            第二次將 main 的 return 位址寫入 one_gadget 並恢復 foo1 的 rbp <br>
            如此一來, main 結束後就會跳到 one_gadget 了 <br>
            
