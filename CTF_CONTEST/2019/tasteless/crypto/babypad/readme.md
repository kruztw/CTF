難度 :  :star:
  
漏洞:

- assert(strlen(plaintext) == strlen(one_time_pad)); 
    * 確保 one_time_pad 不包含 \x00
    * 因此 p[i] != c[i]
       
           
---
  
解題流程:
    
用刪去法, 不斷索取 ciphertext , 直到 p[i] 剩下一種可能
 