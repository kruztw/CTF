![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/RedpwnCTF/forensics/RedPwn%20Gets%20Bamboozled/pic1.png)

想法 : <br>
	開啟 data.txt 後看到 600 800 直覺想到圖片大小<br>
	又看到一大堆 tuple 合理猜測是每個 pixel 的顏色<br>
	(通常 tuple 要麼是座標要麼是顏色, 但重複次數太多不可能是座標) <br>
	畫完圖後打開發現有很多相同大小的圈圈, 只有顏色不一樣 <br>
	利用 [線上汲取工具](https://www.ginifab.com.tw/tools/colors/color_picker_from_image.php) 發現顏色的形式都是 xxxxxx (x = 1 ~ f) <br>
	取出每個顏色的值合併後轉換成 ascii 即可得到 flag <br>
