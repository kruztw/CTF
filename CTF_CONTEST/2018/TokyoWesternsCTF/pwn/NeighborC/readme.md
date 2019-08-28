難度 :  :star::star::star:
  

漏洞: <br>
    fprintf(pFParm1, &DAT_00301060); 存在 fsb 漏洞 <br>


解題流程: <br>
        fsb 在第二個 function 且輸入不放 stack 上, 直接猜 rbp chain <br>
        但這題是 print 到 stderr 所以 local 端看不到, 因此要先將 stderr 的 fileno 改成 1 也就是 stdout <br>
        用 gdb 發現在要執行 fprintf 時的 stack 上有 \*stderr, 我們透過 fsb 漏洞去修改它指向 fileno  並將它改為 1<br>
        再 leak 出該位址就能計算 libc_base <br>
        但由於 aslr 的關係, 這位址 (放 *stderr 的位址) 只能用"猜"的 (機率 1/16)<br>
        之後再利用 fsb 將 malloc_hook 寫入 one_shot <br>
        最後用 fprintf trigger malloc 就能拿到 shell 了 <br>

        
note:
對 file structure 不熟的可以[看這](https://introspelliam.github.io/2018/07/05/pwn/%E6%96%B0%E7%89%88%E6%9C%AClibc%E4%B8%8BIO-FILE%E7%9A%84%E5%88%A9%E7%94%A8/))
        