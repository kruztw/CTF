```
漏洞：
for(i=0; i<6; i++)
		for(j=0; j<6; j++)
			if(lotto[i] == submit[j])
				match++;

沒檢查是否重複

ex:
lotto  : 1 2 3 4 5 6
submit : 1 1 1 1 1 1
=> match = 6

note
submit 為 char
因此要找 ascii 介於 1~45 的符號 或 \x01 也行

```
