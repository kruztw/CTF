```
./auth 內的 win 能 get shell
因此，我們要做的就是想辦法讓程式跳到 win
而題目允許我們更改任意位置，且沒開 PIE
也就是說 win 的位址不會改變
那要怎麼跳過去呢？
其實很簡單，只要改 puts 或 exit 的 got 表即可
```
[got 介紹](http://brandon-hy-lin.blogspot.com/2015/12/shared-library-plt-got.html)

