漏洞:<br>
    
    1. fclose 未檢查返回值 (一般來說，也不太會檢查，但這題是把檢驗碼存入，應當檢查是否寫入成功) <br>

解題流程: <br>

    利用 ulimit 將 file size 設為 0 (ulimit -f 0)<br>
    再用 python 執行即可 <br>

```
$ python
>>> import os
>>> os.system('./otp 0')
```
