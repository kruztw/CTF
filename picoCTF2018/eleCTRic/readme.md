```
漏洞：
1. counter 為定值 (在 AES-CTR 模式，counter 可以讓每次加密出來的結果不同，即便是相同明文)

解題流程

加密
<filename> + .txt 用 AES-CTR mode 加密
加密後的結果再 base64 形成 sharecode

解密
sharecode 先 base64 解密，再用 AES-CTR mode 解密

```

   (AES-CTR)[https://zh.wikipedia.org/wiki/%E5%88%86%E7%BB%84%E5%AF%86%E7%A0%81%E5%B7%A5%E4%BD%9C%E6%A8%A1%E5%BC%8F#/media/File:Ctr_encryption.png]

```

加密方式 cipher = plaintext xor func(key, nonce+counter)

因為 counter = 0 又 key 、nonce 為定值，所以 func(key, nonce) 也是定值

=> 

1. func(key, nonce) = cipher xor plaintext
2. cipher = plaintext xor func(key, nonce)

透過自定義的 filename 和輸出的 base64(cipher), 我們可以得到 func(key, nonce) ( by 1 式)
再將 flagname.txt 和 func(key, nonce) xor 就能得到 cipher 
最後，把 cipher base64 就能得到 sharecode 
拿去解密，即可得到 flag


note:

filename 的長度要和 flagname 的長度一致

```
