// g_buf       0x302060
// g_account   0x302160

void main()
{
  int op;
  uint len;
  undefined pw[136];
  
  init();
  memset(pw, 0, 136);

  while( true ) {
      menu();
      op = get_int();

      switch(op){
        case 1:
            register_account(pw);
            break;

        case 2:
            printf("Login account: ");
            len = _read(g_buf, 152);
            if (!memcmp(&g_buf, &g_account, len)) {
                printf("Password : ");
                len = _read(&g_buf, 152);
                if (!memcmp(&g_buf, pw, len)) // 152 compare 136 ?? bug
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


void menu()
{
  puts("+------------------------------+");
  puts("|             Box++            |");
  puts("+------------------------------+");
  puts("1. register_account");
  puts("2. Login");
  puts("3. Exit");
  puts("Your choice >");
}


void get_int()
{
  char local_28 [24];    
  __read_chk(0,local_28, 0xf, 0x10);
  atoi(local_28);
}


ulong _read(long lParm1,uint uParm2)
{
  uint op;
  
  op = __read_chk(0, lParm1, uParm2, uParm2);
  if (op < 1) {
    puts("read error");
    _exit(1);
  }
  if (lParm1[op - 1] == '\n')
    lParm1[op - 1] = 0;
  
  return op;
}

void log_in()
{
  undefined4 op;
  int len;
  uint idx;
  size_t len;
  int i;
  char box[1864]; // {1: len, 2~233: content , total 8 boxes}
  
  puts("Login successfully.");
  memset(box, 0, 1864);
  while(true){
      menu2();
      op = get_int();
      
      switch(op) {
          case 1:
              for(int i = 0; i<8 && box[i*233]; i++);
      
              if (i < 8) {
                  printf("Put something into the box > ");
                  scanf("%232s", box[i*233 + 1]); //off-by-one
                  len = strlen(box[i*233 + 1]);
                  if (len < 2)
                      box[i*233] = 2;
                  else {
                      len = strlen(box[i*233 + 1]);
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
                   
          if (!box[idx*233+1])
              puts("No such box!");
          else {
              printf("New things > ");
              len = _read(&g_buf, box[idx*233] - 1);
              memcpy(box[idx*233] + 1, &g_buf, len);
              puts("Done!");
          }
          break;

      case 3:
          puts("Not implementeYourd :(");
          break;

      case 4:
          puts("Which box?");
          idx = get_int();
          if (7 < idx) {
              puts("Nop!");
              _exit(-1);
          }
          box[idx*233] = 0;
          memset(box[idx*233] + 1, 0, 232);
          break;

      case 5:
          return;
      }
  }
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



void register_account(void *pvParm1)
{
  memset(&g_account, 0, 136);
  memset(pvParm1, 0, 136);
  printf("Account: ");
  read(0, &g_account, 128);
  printf("Password: ");
  read(0, pvParm1, 128);
  puts("Success!");
}