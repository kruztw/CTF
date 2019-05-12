漏洞 </br>

gets() </br>

解題流程 </br>

1. return 到 open('flag') 上方</br>

結果： 失敗，因為位址有 0xa (換行)</br>

2. rop</br>

結果： 很難控 eax 失敗</br>

3. 跳到 A ~ G 讀出經驗值計算總和，再跳回 ropme 輸入總和</br>

結果： 成功</br>

額外提醒, atoi(num) 當 num 超過 2^64 後，其值為 -1 </br>
