利用 debugfs 檢查 img 

debugfs ./ext-super-magic.img

結果 
./ext-super-magic.img: Bad magic number in super-block while opening filesystem

可見 superblock 的 magic number 發生錯誤


由 hint 看來應該是 ext2 (應該還有其他判斷方式）

在 superblock 有寫 
The superblock is always located at byte offset 1024 from the beginning of the file

且下方有  56    2   s_magic

代表 maigc number 在第 56 57 個 byte

且 s_magic 寫道
16bit value identifying the file system as Ext2. The value is currently fixed to EXT2_SUPER_MAGIC of value 0xEF53.

因此只要在 0x438 (1024 + 56) 寫入 53 EF 即可  (可用 bless 完成）

修復完成後，只須在 mount 到一個資料夾即可

mount ./ext-super-magic.img ./mount 

就可以發現 flag.jpg
