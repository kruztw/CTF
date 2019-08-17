```
leg.c 告訴我們 key = key1() + key2() + key3()

透過 leg.asm 下面這幾行

   0x00008d68 <+44>:	bl	0x8cd4 <key1>
   0x00008d6c <+48>:	mov	r4, r0
   0x00008d70 <+52>:	bl	0x8cf0 <key2>
   0x00008d74 <+56>:	mov	r3, r0
   0x00008d78 <+60>:	add	r4, r4, r3
   0x00008d7c <+64>:	bl	0x8d20 <key3>
   0x00008d80 <+68>:	mov	r3, r0
   0x00008d84 <+72>:	add	r2, r4, r3

我們合理猜測回傳值會紀錄在 r0
因此，只須觀察 key1 2 3 的 r0 是如何被修改的即可

key1
   0x00008cdc <+8> :	mov	r3, pc
   0x00008ce0 <+12>:	mov	r0, r3

r0 = pc = 0x00008ce4

key2
   0x00008d04 <+20>:	mov	r3, pc
   0x00008d06 <+22>:	adds	r3, #4
   ...
   0x00008d10 <+32>:	mov	r0, r3

r0 = pc + 4 = 0x00008d08 + 4 = 0x00008d0c

key3
   0x00008d28 <+8>:	mov	r3, lr
   0x00008d2c <+12>:	mov	r0, r3

r0 = lr = 0x00008d80

因此 key = 0x00008ce4 + 0x00008d0c + 0x00008d80 = 108404

note:
1. arm 的 thumb mode 的 pc 會指到下 2 個指令的位址
2. lr 會紀錄回傳位址

```
