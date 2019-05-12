只要讓 check_password( argv[1] ) 等於 hashcode 就會噴 flag 了

check_password 是將 argv[1] 分成 5 個 int 相加 ( 因為 argv[1] 的長度為 20 byte, 且 ip 的型態為 int )

其中 0x21DD09EC = 0x6c5cec8 * 4 + 0x6c5cecc  ( 用 python 很容易算出來）

但別忘記，資料儲存的格式為 little endian , 也就是 lsb 放在低位元

因此輸入方式如下

./col1 "\xc8\xce\xc5\x06" * 4 + '\xcc\xce\xc5\x06' 

這裡有幾點要注意

1. "c8" => 2 byte  ,   "\xc8"  => 1 byte  (這邊指的是 print 後的結果，否則 "\xc8" 為 4 byte )

2. 不可出現 "\x00" 會被視為終止字元導致長度不等於 20

 

當然，上面的指令是錯誤的，下面提供兩種寫法

1.  ./col    $(python -c 'print "\xc8\xce\xc5\x06"*4 + "\xcc\xce\xc5\x06"')

2.  ./col $(perl -e 'print "\xc8\xce\xc5\x06"x4 . "\xcc\xce\xc5\x06"')
