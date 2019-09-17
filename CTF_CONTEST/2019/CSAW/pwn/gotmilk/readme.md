# ctf writeup

難度 :  :star:
  

漏洞: <br>
    1. printf(local_74) 存在 fsb 漏洞 <br><br>
    

解題流程: <br>
    將 lose got 改成 win got 即可 <br>
    (好像有點短 ... 廢話幾行好了) <br>
    先用 aaaa%p%p%p%p... 找出 aaaa 在第幾個參數 <br>
    再用 fsb 改掉 lose <br>
    btw, lose 的 puts 不參考 puts_got 因為它不定義在 libc.so.6 <br>