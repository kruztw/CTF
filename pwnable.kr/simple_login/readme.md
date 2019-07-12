簡單 reverse 結果放在 question.c <br>

漏洞:<br>

    1. auth 中 tmp 的位址距離 ebp 只有 8 bytes，但 len 最大值為 12, 因此存在 bof 漏洞<br>

解題流程: <br>

    g_buf ( base64 解密出來的存放位置 ) 可分為三個部份 (每一部份佔 4 bytes) <br>
    其中第三部份會寫到 ebp 的值<br>
    因此，將第三部份寫入 g_buf 的位址 <br>
    則在 main 的 leave ( mov esp, ebp; pop ebp ) 會將 esp 寫入 g_buf 的位址<br>
    接著，return 時會再 pop 一次，此時我們就可以控制 eip 了 <br>
