section .text

global asm0

asm0:
	push	ebp
	mov	ebp,esp
	mov	eax,DWORD [ebp+0x8]
	mov	ebx,DWORD [ebp+0xc]
	mov	eax,ebx
	mov	esp,ebp
	pop	ebp	
	ret
