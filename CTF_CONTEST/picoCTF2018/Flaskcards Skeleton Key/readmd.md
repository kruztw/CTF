```
題目告訴我們  secret key (用來加密 session cookie)
合理猜測解題方向在 cookie

將 session cookie 送去解密可得
{u'csrf_token': u'd38d95e7b974c8d006c1c866756b9dba46d650a6',
 u'_fresh': True,
 u'user_id': u'4',
 u'_id': u'7d359a16a057ed96c925ad3c4d079a9f722f2c4e9e09ec33b7fd39dc8bb2e43bf7ba021288e522d1791d4b72f85df16e3b7b219270750ce4a0fcaaf4b79f24ea'
}

將 user_id 改成 1 (通常 admin 是 1)
再拿去加密，可得新的 cookie
修改 cookie 回到 admin 即可得到 flag

note:
```
[flask cookie 加密/解密](https://github.com/noraj/flask-session-cookie-manager)
