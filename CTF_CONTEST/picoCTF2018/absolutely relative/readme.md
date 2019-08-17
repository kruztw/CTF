漏洞
1. file = fopen( "./permission.txt" , "r");

2. while (fscanf(file, "%s", flag)!=EOF)     //少了 ; ???
   fclose(file);
   
 解題流程
 
 permission.txt 為相對路徑
 因此只要在能寫入的地方建立 permission.txt 並輸入 yes
 且在該位置執行，即可繞過檢查
 
 
 
