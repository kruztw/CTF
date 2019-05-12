```
漏洞
scanf("%d", passcode1); 沒有 ＆
因此，passcode1 的值會被當作位址，並寫入該位址

解題流程

目標：
將 passcode1 寫入 338150, passcode2 寫入 13371337

login 沒有任何地方可寫入 passcode1 和 passcode2
因此合理猜測 welcome 的 name 應該能蓋到 (哪國人的名字需要用到 100 個字元阿？？)
經過測試後發現
name 的最後 4 個 byte 會蓋到 passcode1
但...passcode2 依舊沒辦法

因此，目標無法達成

換個想法，既然 passcode1 的值可控
而且又有 scanf("%d", passcode1)
這不就代表可做到任意位址寫入嗎？？
可想而知，這題應該是 got hijacking
將 fflush 的 got 改成 system("/bin/cat flag") 的位址，就能拿到 flag 了

```
