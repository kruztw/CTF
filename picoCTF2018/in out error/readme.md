題目將 flag.txt 的內容輸入到 stderr

因此只要將 stderr(2) 的內容導到某個檔案內即可

./in-out-error 2>/tmp/flag

note:
stdin  0
stdout 1
stderr 2
