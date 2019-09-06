難度 :  :star::star::star:
  

漏洞: <br>
    1. free 後可以修改 chunk (uaf) <br><br>
    

解題流程: <br>

<b><法一(難) 針對 Full RelRo></b><br>
        先在 name 偽造兩塊 chunk, 再用唯一一次的修改機會拿到 name <br>
       將 name free 掉, 在此之前別忘了先將 tcache 塞滿 <br>
       利用 malloc_consolidate 將 name 放到 small bin <br>
       此時 name 的 fd 和 bk 都會指向 small bin <br>
       因此我們可以用 partial write fd 拿到 stdout 附近的 chunk <br>
       但在此之前, 必須要讓 fastbin 內有 name 的 chunk, 很可惜並沒有 <br>
       因此我們要先 free 掉 name, 但這樣一來 fd 就會被改成 0 <br>
       所以我們可以先要一塊小 chunk , 這塊 chunk 會從 name 這塊去切<br>
       如果我們要 0x10 的 chunk 則會切 0x20 的大小, 使得 small bin 指到 name + 0x20<br>
       幸運的是, name+0x20 已經在 fastbin 裡 (其實早就算好了😎) <br>
       部份修改 fd 就能拿到 stdout 附近的 chunk 了 <br>
       但要注意的是 getnline 會將最後一個字元設成 \x00 <br>
       所以 malloc 時要注意, 不能讓 \x00 的位置出現在重要的地方 <br>
       這樣會有很高的機率出錯, 但總比一定會錯來的好 <br>
       拿到後, 修改 \_IO\_wrtie\_base 就能 leak 出 libc_base 的位址 <br>
       計算 \_\_malloc\_hook 並寫入 one\_shot 
       再次 malloc (注意 size 要超過 0x800), 就能拿到 shell 了 <br>
<br><br>
<b><法二(易) 修改 got></b> <br>
    先在 name 偽造兩塊 chunk, 再用唯一一次的修改機會拿到 name <br>
    透過 rename 和 atoi 的位址拿到 chunk, 並在下方寫入 0x71 <br>
    畢竟一次寫不到, 我們拿兩次 <br>
    修改 lock 和 key 一致, 這樣就能無限次修改 <br>
    並在 list 寫入 free 和 puts 的 got <br>
    修改 free got 為 puts plt, 並 free 掉 puts got 那塊 (別忘了此時 free 就是 puts) <br>
    計算 libc 位址並將 one shot 填入 puts got <br>
    等到運行到 puts 時就能 get shell 了 <br>


note:<br>
    原本打算給 4 顆星, 但 got 能改, 所以只給 3 顆