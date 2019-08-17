```
check_password:

44bc:  0e43           clr	r14                                  ; i = 0
44be:  0d4f           mov	r15, r13                             ; r13 = &password[0]
44c0:  0d5e           add	r14, r13                             ; r13 = &password[i]
44c2:  ee9d 0024      cmp.b	@r13, 0x2400(r14)                  ; *(0x2400+i) == password[i] ?
44c6:  0520           jne	#0x44d2 <check_password+0x16>        ; no: goto 0x44d2
44c8:  1e53           inc	r14                                  ; i += 1
44ca:  3e92           cmp	#0x8, r14                            ; i == 8 ?
44cc:  f823           jne	#0x44be <check_password+0x2>         ; no: goto 0x44be
44ce:  1f43           mov	#0x1, r15                            ; r15 = 1 ( 檢查完畢 )
44d0:  3041           ret                      
44d2:  0f43           clr	r15                                  ; r15 = 0 ( 有誤 )
44d4:  3041           ret

因此，password = 0x2400 ~ 0X2400 + 7

我的是 :  6b7b2b364a3257  ( 可能不一樣 )
```
