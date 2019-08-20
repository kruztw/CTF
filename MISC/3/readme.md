# 步驟 : 

## 找出 profile

<b> volatility -f husky_memory.raw imageinfo </b>

得知 profile 為 WinXPSP2x86

## 用 cmdscan 看看下了什麼指令 ( 註: 也可以先用 timeliner 看看近期的變化 )

<b>volatility -f husky_memory.raw --profile=WinXPSP2x86 cmdscan</b>

發現多了一個 "hu5ky_4nd_f0r3n51c" 的資料夾

## 用 filescan 找出該資料夾的位置

<b>volatility -f husky_memory.raw --profile=WinXPSP2x86 filescan | grep hu5ky_4nd_f0r3n51c</b>

## 用 dumpfiles 把內容印出來

<b>volatility -f husky_memory.raw --profile=WinXPSP2x86 dumpfiles -Q 0x0000000002c5dd18 -D .</b>

得到 file.None.0x826a7488.dat

## 用 vim %!xxd 看看

<b> vim file.None.0x826a7488.dat ( :%!xxd )

發現 (!raR 在 000000d8)
(註: 離開用 %!xxd -r )

## 將該段萃取出來並反轉

<b>dd if=file.None.0x826a7488.dat of=output bs=1 count=220</b>
<b><output xxd -p | tac | xxd -r -p > output.rar</b>

## 剩餘工作

<b>strings husky_memory.raw | grep password</b>
<b>rar e output.rar (密碼: hu5ky_4nd_f0r3n51c)</b>

