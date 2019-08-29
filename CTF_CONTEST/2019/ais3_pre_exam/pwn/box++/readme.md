難度 :  :star::star::star:
  

漏洞: <br>
    1. memcmp(&g_buf, pw, len);  len 的長度超過 pw, 會導致 memory leak<br>
    2. scanf("%232s", box[i]+1); 存在 off-by-one


解題流程: <br>
		這題跟 box 幾乎一樣, 差別在沒有 show <br>
        show 的部份可以用第一個漏洞取代<br>
