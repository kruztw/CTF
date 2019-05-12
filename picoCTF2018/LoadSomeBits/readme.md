```
題目說 lsb 可能存在 flag
因此我們將每一個 byte 的 lsb 取出，並且位移 (不確定從哪個 byte 開始才對)

note:
位移最多 1 byte 也就是 8 個 bits
因為從第 9 個 bit 開始，就相當於從第 1 個 bit 開始並扣除第一個 byte
```
