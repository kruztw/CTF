解題流程

e = 3 (很小 => 存在 Low public exponent attack)
m = c 開 3 方

[論文](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/rsa.pdf)
 

note 1:
我只看得懂第一部份，第二部份證明看不太懂QQ (希望以後看得懂)

簡單描述
A 想傳 m 給 B C D
為了提昇速度，所以選用很小的 e
假設 NB NC ND 分別為 B C D 選用的公鑰
由 RSA 加密過程可知

C1 = m^3^ (mod NA)
C2 = m^3^ (mod NB)
C3 = m^3^ (mod NC)

透過中國餘數定理可得 m^3^  (請參考離散數學)
將計算出來的數開 3 方即可得到 m

簡單說明 part2 
上面之所以會被攻破都是因為使用相同 m 去加密
如果我們讓 m 每次都不一樣不就 ok 了
怎麼做呢？
很簡單，就令 m = m+2^k^ * ID  (ID 會隨接收者改變, k 是常數)
接著 part2 就告訴你，當蒐集的數據 (C 和 N) 夠多時，它仍然會被 part1 類似的方式破解



note 2:
求 m 可用 gmpy2 提供的大數運算

sudo apt install libgmp-dev libmpfr-dev libmpc-dev (如果有 libc-brabrabra 的 error 時可試試）
sudo pip3 install gmpy2
