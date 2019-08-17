```
448a <check_password>
448a:  bf90 666d 0000 cmp	#0x6d66, 0x0(r15)               ; password[0:1] == 0x6d66?
4490:  0d20           jnz	$+0x1c                          ; no : goto $sp+0x1c
4492:  bf90 7523 0200 cmp	#0x2375, 0x2(r15)               ; password[2:3] == 0x2375?
4498:  0920           jnz	$+0x14                          ; no : goto $sp+0x14
449a:  bf90 2222 0400 cmp	#0x2222, 0x4(r15)               ; password[4:5] == 0x2222?
44a0:  0520           jne	#0x44ac <check_password+0x22>   ; ; no : goto 0x44ac
44a2:  1e43           mov	#0x1, r14                       ; r14 = 1
44a4:  bf90 5c31 0600 cmp	#0x315c, 0x6(r15)               ; password[6:7] == 0x315c?
44aa:  0124           jeq	#0x44ae <check_password+0x24>   ; yes : goto 0x44aae
44ac:  0e43           clr	r14                             ; r14 = 0
44ae:  0f4e           mov	r14, r15                        ; r15 = r14
44b0:  3041           ret

因此 password = 6d6623752222315c 
錯，為什麼？
因為這個系統除存資料的方式為 little endian
因此，6d66 讀出來事實上是 666d (此處的 cmp 單位為 16 
所以 pasword 應為
password : 666d752322225c31
```
