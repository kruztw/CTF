fd 減完 0x1234 會被放在 read 第一個參數

不難猜出 fd 所代表的意思就是 file descriptor

詳情請見 http://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/

常用的有 

0 : stdin

1 : strout

2 : stderr

 

因此，只要讓 argv[1] = 0x1234 , fd 就會等於 0

接著在輸入 LETMEWIN 就能拿到 flag 了
