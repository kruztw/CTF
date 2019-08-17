```
AES-CBC 有二種主要攻擊方式

1. padding oracle
2. bit-flipping


此題考 bit-flipping

簡介
AES-CBC 加密是將 block 與前一塊的密文 xor 後，再加密
第一塊則是跟 IV xor

解密則是先解密，再 xor
因此，如果我們改變前一塊的密文，則 xor 出來的結果也會隨之改變
但問題是...前一塊解密出來不也會變嗎？
對阿，但如果前一塊是 IV 就沒差了 (因為 IV 不用解密)


使用時機：
已知明文跟密文

bit-flipping 主要是用來修改明文而不是猜出明文
以這題來說，我們要將 admin=0 改成 admin=1

怎麼做呢?
由原始碼得知，cookie 加密完後還會 base64
因此，先將 cookie debase64
再將第 11 個 byte + 1 或 - 1
為什麼是第 11 個 byte

{'admin': 0
12345678910 => 0 在第 11 個 byte

+1 還是 -1 ？
我們的目的是要讓最後一個 bit 反向，因此如果是奇數，則-1, 偶數則 +1
假設要修改的值的 16 進位為 b4
ex: b4 -> b5 => admin=1
    b4 -> b3 => admin=7
   
原本 xor 出來 admin=0 => intermidary value = b4
因此 b4 xor b5 = 1
    b4 xor b3 = 7

```
