question.c : 簡易 reverse 後的 code

漏洞: <br>
1. my_hash 將 canary 拿去做運算，使得 canary 可被逆向求出<br>
2. g_buf 大小為 0x400 , 經過 base64 decode 後，長度變為原來的 3/4 倍, 也就是 0x300 大於 buf 的長度 ，形成 BOF <br>


解題過程：<br>
  先算出 canary ，在將 return address 改成 system 的位址，並塞入 sh <br>
  則 return 後，便會觸發 system("sh") <br>

payload 解析 : <br>
```  
  b64e('a'*512 + p32(int(canary, 16)) + 'a'*12 + p32(system) + p32(g_buf+537*4/3) + '=') + "sh\0\0"
  先將 buf 塞滿，並透過組語可知，canary 的位址在 ebp-0xc
  因此塞入 canary 後還有 0xc 的空間才到 return address
  將 return address 塞入 system
  且 esp 必須指向內容為 sh 的位址，因此塞入 p32(g_buf+537*4/3)
  537 = 512 (a) + 4 (p32) + 12 (a) + 4 (p32) + 4 (p32) + 1 (=)
  之所以塞 = 是為了讓大小為 3 的倍數
  乘 4/3 是因為 base64 後，長度會變為原來的 4/3 倍
```

int(time.tim()) 的位置 <br>

因為 time(NULL) 是以秒為單位<br>
所以這行與觸發 hash 的位置愈近愈好 (只要時間間隔在 1s 內就行惹)<br>
 
