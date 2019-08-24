  難度 :  :star: 
  
  ![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/crypto/OTP/pic1.png)

解題想法 : <br>
	題目提示說明 "meme" 在兩個字串皆被使用 <br>
    這代表著如果我們把 c1 和 c2 和 meme 做 xor <br>
    分別會有 4 個連續字的明文 <br>
    要注意的是, meme 的順序可能是 meme 或 emem <br>
    而我們得到的結果是 <br>
    \`+rqudanY[reyoeb<oc <br>
    說真的看很久都看不出明文 , 最後才發現 udan 和 reyo 是明文 <br>
    怎麼發現的呢？ <br>
    因為看不出來, 因此乾脆猜明文開頭為 d4rk{  , 結果得到 areyo 開頭 <br>
    再一步步推下去得到明文為 "d4rk{meme__meme}c0de" <br>
    