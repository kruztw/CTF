```
原本以為 test_password_valid 很可疑
但跟進去後發現，他根本和 password 無關
因此不管輸入什麼，出來後 r15 都會等於 0
接著往下看，發現有一行很奇怪

4548:  0f93           tst	r15
454a:  0324           jz	$+0x8
454c:  f240 d500 1024 mov.b	#0xd5, &0x2410
4552:  3f40 d344      mov	#0x44d3 "Testing if password is valid.", r15
4556:  b012 de45      call	#0x45de <puts>
455a:  f290 e400 1024 cmp.b	#0xe4, &0x2410         ; ？？？？ 這位址好像寫得到
4560:  0720           jne	#0x4570 <login+0x50>
4562:  3f40 f144      mov	#0x44f1 "Access granted.", r15
4566:  b012 de45      call	#0x45de <puts>
456a:  b012 4844      call	#0x4448 <unlock_door>

因此，我們只要將 0x2410 寫入 e4 即可破關 

(0x2410 在 password 寫入範圍)
```
