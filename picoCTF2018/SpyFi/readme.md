AES ECB 模式下，相同明文會對應相同密文

![ECB 加密方法](https://zh.wikipedia.org/wiki/%E5%88%86%E7%BB%84%E5%AF%86%E7%A0%81%E5%B7%A5%E4%BD%9C%E6%A8%A1%E5%BC%8F#%E7%94%B5%E5%AD%90%E5%AF%86%E7%A0%81%E6%9C%AC%EF%BC%88ECB%EF%BC%89)
```
因此只要精心設計，就能用暴力破解找出明文

message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {1}.
Down with the Soviets,
006
""".format( sitrep, agent_code )

message 是要加密的明文
{0} 的部份由我們控制
{1} 的部份為 flag

由 pad 可知，block 長度為 16 個字元
因此加密後每一 block 會對應 32 個 hex

將 message 16 個一組分成若干個 block，如下所示

Agent,\nGreetings
. My situation r
eport is as foll
ows:\n{0}
\nMy agent identi
fying code is: {1}
.\nDown with the 
Soviets,\n006

為了方便起見，我們用 a 將 ows 那行填滿

Agent,\nGreetings
. My situation r
eport is as foll
ows:\naaaaaaaaaaa     (11 個 a)
{0}
\nMy agent identi
fying code is: {1}
.\nDown with the 
Soviets,\n006

因此，如果 {0} 用 fying code is: p 代入，則 block 5 和 block 7 加密出來的結果會一樣 ( {1} 為 picoCTF{...} )

但 p 要怎麼猜呢？ (假設我們不知道 {1} 的開頭為 p)
我們就必須將所有可能代入，若加密結果 block 5 和 block 7 一致，就代表猜對了

p 有了，那怎麼猜 i 呢?
這需要些技巧，必須將 {0} 用 aa...a {0} aa..a 代換，如下所示

Agent,\nGreetings
. My situation r
eport is as foll
ows:\naaaaaaaaaaa     (11 個 a)
{0}
aaaaaaaaaaaaaaaa
\nMy agent identi
fying code is: {1}
.\nDown with the 
Soviets,\n006

同樣的我們將 {0} 用 fying code is: p 代入，則 block 5 和 block 8 加密出來的結果會一樣 
接著我們讓上下兩行的 a 都少一個

Agent,\nGreetings
. My situation r
eport is as foll
ows:\naaaaaaaaaaf     (10 個 a)
{0}
aaaaaaaaaaaaaaa\n
My agent identif
ying code is: {1}
.\nDown with the 
Soviets,\n006

此時 block 5 就變 ying code is: pi 且加密後與 block 7 仍然一致
如此繼續，就能將 flag 找出來了

note:
再次強調，加密後一個 block 為 32 hex (這對 exp.py 的理解應該會有幫助)
```
