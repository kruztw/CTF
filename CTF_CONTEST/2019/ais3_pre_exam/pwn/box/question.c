// g_account     0x302160
// g_buf 0x302060

void main()
{
    int op;
    uint len;
    undefined pw [136];
    undefined8 local_10;
  
    init();
    while( true ) {
        menu();
        op = get_int();
        switch(op){
            case 1:
                register_account(pw);
                break;

            case 2:
                printf("Login account: ");
                len = _read(&g_buf, 152); 
                if(!memcmp(&g_buf, &g_account, len)){ // bug!! 152 cmp 136
                    printf("Password : ");
                    len = _read(&g_buf, 152);
                    if (!memcmp(&g_buf, pw, len))
                        log_in();
                    else
                        puts("Wrong password!");
                }
                else 
                    puts("No such user!");
                break;

            case 3:
                break;
        }
    }
    puts("Bye.");
    _exit(0);
}


void init()
{
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
}


void get_int()
{
  char local_28 [24];
  __read_chk(0, local_28, 15, 16);
  atoi(local_28);
}

void menu()
{
  puts("+-----------------------------+");
  puts("|             Box             |");
  puts("+-----------------------------+");
  puts("1. Register");
  puts("2. Login");
  puts("3. Exit");
  puts("Your choice >");
}

ulong _read(long _buf,uint _len)
{
  uint len;
  
  len = __read_chk(0, _buf, _len, _len);
  if(_buf[len-1] == '\n')
      _buf[len-1] = 0;

  return len;
}


void log_in()
{
    undefined4 op;
    int len;
    uint idx;
    size_t len;
    char box[1864]; // 1: length, 2-233: content, total 8 boxes
  
    puts("Login successfully.");
    memset(box,0, 1864);
    menu2();
    op = get_int();
    while(true){
        switch(op) {
            case 1:
                for(int i = 0; i<8 && box[i*232]; i++);
              
                if (i < 8) {
                    printf("Put something into the box > ");
                    scanf("%232s", &box[i*232+1]); // off-by-one
                    len = strlen(box[i*232+1]);
              
                    if (len < 2) 
                        box[i*233] = 2;
                    else {
                        len = strlen(box[i*233+1]);
                        box[i*233] = len;
                    }
                }
                else
                    puts("No more box!");
                    break;
            case 2:
                puts("Which box?");
                idx = get_int();
                if (7 < idx) {
                    puts("Nop!");
                    _exit(-1);
                }
                if(!box[idx*233+1])
                    puts("No such box!");
                else {
                    printf("New things > ");
                    len = _read(&g_buf, box[idx*233] - 1);
                    memcpy(box[idx*233+1], &g_buf, len);
                    puts("Done!");
                }
                break;
          
            case 3:
                for(int i = 0; i<8; i++)
                    if(box[i*233])
                        printf("[Box %d] %s\n", i, box[i*233+1]);
              
                break;
          
            case 4:
                puts("Which box?");
                idx = get_int();
                if (7 < idx) {
                    puts("Nop!");
                    _exit(-1);
                }
                box[idx*233] = 0;
                memset(box[idx*233+1], 0, 232);
                break;
            
            case 5:
                return;
        }
    }
}


void register_account(void *_pw)
{
  memset(&g_account, 0, 136);
  memset(_pw, 0, 136);
  printf("Account: ");
  read(0,&g_account, 128);
  printf("Password: ");
  read(0, _pw, 128);
  puts("Success!");
}


void menu2()
{
  puts("1. new box");
  puts("2. update box");
  puts("3. view all box");
  puts("4. delete box");
  puts("5. Logout");
  puts("Your choice >");
}
