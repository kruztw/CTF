漏洞:</br>

gets 存在 bof </br>

解題流程: </br>

想法一 </br>

使 BK = return address , FD = shell</br>
則 BK->fd = FD <=> return address = shell </br>
問題: FD->bk = BK <=> shell + 4 = return address  (shellcode 被破壞了) </br>

</br>
想法二</br>
利用這二行 (反組譯後可見)</br>

```
0x080485ff <+208>:	mov    ecx,DWORD PTR [ebp-0x4] 
0x08048603 <+212>:	lea    esp,[ecx-0x4]
```

如果 [ecx-0x4] == shell 則 esp = shell => return 到 shell</br>
方法 : [ebp-0x4] = shell + 4</br>

![alt structure](https://github.com/dreamisadream/CTF/blob/master/pwnable.kr/unlink/source/unlink1.png)




