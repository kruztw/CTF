# ctf writeup

難度 :  :star::star:
  

漏洞: <br>
    1. if (idx < tIndex) 沒檢查 idx 是否 < 0 (out of bound) <br>
    2. trips[idx]->destination[len] = 0; 存在 off-by-one <br><br>
    

解題流程: <br>
* 前言<br>
        原本不打算寫這題的 writeup (因為比賽寫好的腳本, 在結束後測試別人的 writeup 時覆蓋掉惹 QQ) <br>
        但由於 [這個 writeup](https://ctftime.org/writeup/16469) 太猛了, 所以紀錄一下 <br>
        瞭解這個東西後, 這題根本躺著解 \_(:3 ⌒ﾞ)_  <br>
        
* 正文<br>
        在 text 段內有個 \_\_DT_JMPREL , 這個位址記載各個 library call 的  got 的存放位址 <br>
        透過這個位址並用漏洞 1 , 修改 free got 為 system,  剩下的就不多說了 <br>
        需要特別注意的是 trips[idx]->destination 的取值方式<br>
        必須讓 trips[idx] 的值為 __DT_JMPREL , 這樣 -> destination 才會是 free got<br>
        而  idx 則是 buf(存 __DT_JMPREL 的位址) 到 trips 的差值除以 8 (詳情請用 gdb 自己 trace ) <br>
        
* 另解<br>
    利用 off-by-one shrink the chunk<br>
    這個攻擊沒有圖示不好懂, 所以詳情請見 Angelboy 大大 [這篇](https://www.slideshare.net/AngelBoy1/advanced-heap-exploitaion) 的 shrink the chunk (25 頁) 的部份 <br>
        