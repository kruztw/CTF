[zip 偽加密](https://blog.csdn.net/kajweb/article/details/76474476) </br>
[zip 格式](https://blog.csdn.net/wclxyn/article/details/7288994) </br>

首先，我們用 bless or hexedit 打開 flag.zip </br>
接著搜尋 50 4B  也就是文件頭標記的位址 ( 用 little endian 表示 ) </br>
我們發現壓縮文件數據區的全局方式位標記為 00 00 (無加密) </br>
但目錄區卻是 09 00 (有加密) </br>
可見這是一個偽加密的 zip 檔 </br>
將目錄區的 09 00 改成 00 00 </br>
就能解壓縮惹 </br>

至於解壓縮出來的內容就不用管了 </br>
想知道可看 exp.py </br>


