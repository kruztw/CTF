```
利用 IDA 反組譯後可發現 do_magic 就是將輸入的字串跟 0x8048858 的字串做 xor
如果等於 greetingMessage 則印出 You are winner!
```

![image](https://github.com/dreamisadream/CTF/blob/master/picoCTF2018/quackme/quackme1.png)

```
說好的 flag 呢？
試了之後就會發現，輸入了的字串即為 flag

至於 0x8048858 的字串怎麼取得呢？
1. IDA
2. gdb
```
