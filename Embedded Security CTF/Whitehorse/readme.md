```
經過測試後得知 password 第 17 個 byte 可控制返回位址
而我們的目的是 unlock door
由前面幾題得知
unlock door 須傳入參數 0x7f 並呼叫 INT   ( 4460:  b012 3245      call	#0x4532 <INT> )

因此 password 為 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa60447f00
```
