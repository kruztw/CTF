```
section .text	
global asm2

asm2:
	push   	ebp                         
	mov    	ebp,esp
	sub    	esp,0x10
	mov    	eax,DWORD [ebp+0xc]        ; eax = 0x28
	mov 	  DWORD [ebp-0x4],eax        ; *(ebp-0x4) = 0x28
	mov    	eax,DWORD [ebp+0x8]        ; eax = 0x7
	mov	    DWORD [ebp-0x8],eax        ; *(ebp-0x8) = 0x7
	jmp    	part_b
part_a:	
	add    	DWORD [ebp-0x4],0x1        ; *(ebp-0x4) = *(ebp-0x4) + 0x1
	add	    DWORD [ebp+0x8],0x76       ; *(ebp+0x8) = *(ebp+0x8) + 0x76
part_b:	
	cmp    	DWORD [ebp+0x8],0xa1de     ; 0x7 == 0xa1de ??
	jle    	part_a                     ; taken => goto part_a
	mov    	eax,DWORD [ebp-0x4]        ; eax = *(ebp-0x4)
	mov	esp,ebp
	pop	ebp
	ret

上面做的事簡單來說就是將 *(ebp + 0x8) 不斷加 0x76 直到大於 0xa1de
每加一次就將 *(ebp-0x4) 加 1
然後輸出 *(ebp-0x4)

輸出 ＝ 0x28 + 0xa1de // 0x76 + 1 = 392 
```
