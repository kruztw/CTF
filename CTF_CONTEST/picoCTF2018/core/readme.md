```
OS 會將因為 signal 而被 terminate 的 process 的資訊存放在 core
```

[core 簡介](https://zh.wikipedia.org/wiki/%E6%A0%B8%E5%BF%83%E8%BD%AC%E5%82%A8)
```
因此，透過  gdb ./print_flag ./core  就能找出被終止前的資訊

另外，print_flag 的 print_flag 告訴我們，flag 的位置被放在 0x804a080 + 4*0x539

所以只要用 gdb ./print_flag ./core 並輸入 x/sb *(0x804a080+4*0x539) 即可看到 flag
```
