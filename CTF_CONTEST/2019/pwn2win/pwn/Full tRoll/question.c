void main()
{
    char pw [32];
    char answer [40];
  
    addr = (char *)malloc(16000);
    memset(pw, 0, 48);
    memset(answer, 0, 40);
    setvbuf(stdout,(char *)0x0,2,0);
    read_flag(answer);
    while( true ) {
        while( true ) {
            while( true ) {
                while( true ) {
                    puts("Welcome my friend. Tell me your password.");
                    _read(stdin, pw);
                    result = check_pw(pw);
                    if (result != 1 && result != 2) break;
                    analyze((ulong)result, 0);
                }
                result = compare(answer);
                if (result != 0) break;
                analyze(3,answer);
            }
            fd = fopen(answer,"rb");
            if (fd == (FILE *)0x0) break;
            _read(fd, addr);
            puts(addr);
            fclose(fd);
        }
        if(answer[0] == '\0') break;
        analyze(3,answer);
    }
    analyze(4,0);
    return 0;
}



void read_flag(char *param_1)
{ 
  __src = getenv("FLAG_FILE");
  if (__src == (char *)0x0)
      strcpy(param_1,"secret.txt");
  else 
      strcpy(param_1, __src);
}


ulong _read(FILE *param_1,long param_2)
{
    i = 0;
    while( true ) {
        cVar1 = fgetc(param_1);
        if (cVar1 == -1 || cVar1 == '\n') break;
        param_2[i] = cVar1;
        i = i + 1;
    }
    return (ulong)i;
}


undefined8 check_pw(byte *param_1)
{ 
    len = strlen(param_1);
    if (len < 23)
        return 1;
    else {
        if (((((((param_1[1] ^ *param_1) == 0x3f) && ((param_1[2] ^ param_1[1]) == 0xb)) &&
          ((param_1[3] ^ param_1[2]) == 0x27)) &&
         ((((param_1[4] ^ param_1[3]) == 0x33 && ((param_1[5] ^ param_1[4]) == 0x41)) &&
          (((param_1[6] ^ param_1[5]) == 0x4f &&
           (((param_1[7] ^ param_1[6]) == 0x3b && ((param_1[8] ^ param_1[7]) == 0x1b)))))))) &&
        (((param_1[9] ^ param_1[8]) == 0x21 &&
         (((((((param_1[10] ^ param_1[9]) == 0x32 && ((param_1[0xb] ^ param_1[10]) == 0x73)) &&
             ((param_1[0xc] ^ param_1[0xb]) == 0x79)) &&
            (((param_1[0xd] ^ param_1[0xc]) == 0x2b && ((param_1[0xe] ^ param_1[0xd]) == 0x3a)))) &&
           ((param_1[0xe] == param_1[0xf] &&
            (((param_1[0x10] ^ param_1[0xf]) == 2 && ((param_1[0x11] ^ param_1[0x10]) == 0x38))))))
          && ((param_1[0x12] ^ param_1[0x11]) == 0x1d)))))) &&
       (((((param_1[0x13] ^ param_1[0x12]) == 3 && ((param_1[0x14] ^ param_1[0x13]) == 4)) &&
         ((param_1[0x15] ^ param_1[0x14]) == 0x49)) &&
        (((param_1[0x16] ^ param_1[0x15]) == 0x61 && (param_1[0x16] == 0x58))))))
            return 0;
        else
            return 2;
  }
}


void analyze(int param_1,undefined8 param_2)
{
  if (param_1 == 1)
      puts("Not even close!\n");
  else if (param_1 == 2) 
      puts("Incorrect!\n");
  else if (param_1 == 3)
      printf("Unable to open %.*s file!\n",0x30,param_2);
  else
      printf("Unknown error");
}


undefined8 compare(char *param_1)
{ 
    j = 0;
    do {
        len = strlen(param_1);
        if (len <= (ulong)(long)j)
            return 1;
        
        same = false;
        i = 0;
        while (len = strlen(s_abcdefghijklmnopqrstuvwxyzABCDEF_00302020), i < len) {
            if (s_abcdefghijklmnopqrstuvwxyzABCDEF_00302020[i] == param_1[j]) {
                same = true;
                break;
            }
            i = i + 1;
        }
        if (!same)
            return 0;
          j = j + 1;
      } while( true );
}