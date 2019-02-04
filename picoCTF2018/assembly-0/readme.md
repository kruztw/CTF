注意要點
1. x86 會將返回資料放在 eax
2. 呼叫副程式時會 create 一塊稱為 procedure frame (activation record) 用來紀錄參數和返回位址等
3. 參數的存取大多藉由 ebp (base pointer) + offset (因為 ebp 位址固定方便組譯器組譯)
4. 參數 push 順序由後往前

根據 4 得知，ebp + 0x8 存放 0xd8 , ebp + 0xc 存放 0x7a

```
asm0:
	push	ebp
	mov	ebp,esp
	mov	eax,DWORD [ebp+0x8]    ; eax = 0xd8
	mov	ebx,DWORD [ebp+0xc]    ; ebx = 0x7a
	mov	eax,ebx                ; eax = 0x7a
	mov	esp,ebp
	pop	ebp	
	ret                        ; 回傳 0x7a = 122
```


如果懶的看也可以直接執行
nasm -f elf32 <intro_asm_rev.S.S>
gcc exp.c intro_asm_rev.o -m32

若用 nasm 必須先將組合語言改成相容形式

