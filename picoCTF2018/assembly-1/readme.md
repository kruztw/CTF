```
section .text

global asm1

asm1:
	push	ebp
	mov	ebp,esp
	cmp	DWORD [ebp+0x8],0x98  ; cmp 0x76, 0x98  <
	jg 	part_a	              ; not taken
	cmp	DWORD [ebp+0x8],0x8   ; cmp 0x76, 0x8
	jne	part_b                ; taken
	mov	eax,DWORD [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD [ebp+0x8],0x16
	jne	part_c
	mov	eax,DWORD [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:
	mov	eax,DWORD [ebp+0x8]    ; eax = 0x76
	sub	eax,0x3                ; eax = 0x73
	jmp	part_d                 ; let's go
	cmp	DWORD [ebp+0x8],0xbc
	jne	part_c
	mov	eax,DWORD [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD [ebp+0x8]
	add	eax,0x3
part_d:
	pop	ebp                  
	ret                         ; eax = 0x73 = 115
```

也可以直接用 c 執行 (參考 assembly-0)
