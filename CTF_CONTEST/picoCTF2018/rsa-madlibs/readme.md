```
照著 rsa 的方法做就行了

網路上看到很精簡(厲害)的寫法
MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

lambda 參數 : 陳述句

先備知識 short circuiting evaluation

如果 n < 2 發生則檢查 t%N ，若 t%N 不為 0 (false) 則回傳 t%N (略過後面 MMI(...) 的部份)
否則，執行 MMI(....)

```


