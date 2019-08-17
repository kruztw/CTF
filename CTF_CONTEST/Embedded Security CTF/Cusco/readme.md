```
跟 Hanoi 類似
差別在這次問題出在 ret 的位址會被 password 蓋掉
因此只要在 ret 的位址寫入 unlock_door 的位址即可

note
注意 little endian
假設 unlock_door 在 0x4446
那麼 ret 位址要寫入 4644

```
