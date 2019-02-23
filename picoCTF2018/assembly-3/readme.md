```
section .text
	global asm3

asm3:
	push   	ebp
	mov    	ebp,esp
	mov	eax,0x19
	xor	al,al			;al=0
	mov	ah,BYTE [ebp+0xa]    	;ah=0xe8
	sal	ax,0x10			;ax=0
	sub	al,BYTE [ebp+0xd]	;al=-0x8a = 0x76
	add	ah,BYTE [ebp+0xc]	;ah=0x95  (ax = 0x9576)
	xor	ax,WORD [ebp+0x12]	;ax=0x9576 xor 0xe207 = 1001010101110110 xor 1110001000000111 = 0x7771
	mov	esp, ebp
	pop	ebp
	ret

note:

nasm -f elf32 <filename>.S
gcc <filename>.c -o <output> <filename>.o -m32
./<output>

ebp 指向 ebp
ebp + 0x4 指向 return address
ebp + 0x8 指向 0xb5e8e971
ebp + 0xc 指向 0xc6b58a95
ebp +0x10 指向 0xe20737e9

little endian =>
ebp + 0x8 : 0x71
ebp + 0x9 : 0xe9
ebp + 0xa : 0xe8
ebp + 0xb : 0xb5

WORD = 2 BYTE ( 以這題來說 )

```

