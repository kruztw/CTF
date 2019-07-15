漏洞: <br>
    
    1. dragon HP 的型態為 char 很容易 overflow <br>

    2. dragon 、player 被擊敗時，function pointer 沒設成 NULL 就 free <br>

    3. dragon 若被擊敗，則在輸入 name 時，會拿到剛剛 free 掉的 chunk (因為大小一樣，且都屬於 fast_bin) <br>

解題流程: <br>

	先 overflow Mama dragon ，再把 Mama dragon chunk 的 function_ptr 改成 system("/bin/sh") 那行 <br>


