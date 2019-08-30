// g_name 0x602060
// g_ptr 0x602088

void main()
{
    long op;
    uint i;
  
    init();
    printf("Name:");
    _read(&g_name,0x20);

    i = 0;
    while( true ) {
        menu();
        op = read_int();
        switch(op){
          case 1:
              add();
              break;

          case 2:
              if (i < 8) {
                  free(g_ptr);
                  i = i + 1;
              }

          case 3:
              show();
              break;

          case 4:
              exit(0);

          default:
              puts("Invalid choice");
        }
    }
}



void init()
{
  setvbuf(stdin,(char *)0x0,2,0);
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stderr,(char *)0x0,2,0);
  signal(0xe,FUN_00400927);
  alarm(0x3c);
}




void _read(long lParm1,uint uParm2)
{
  int iVar1;
  iVar1 = __read_chk(0, lParm1, uParm2, uParm2);
  if (iVar1 < 1) {
    puts("read error");
    _exit(1);
  }
  if (lParm1[iVar1-1] == '\n')
      lParm1[iVar1-1] = 0;
}


void menu()
{
  puts("$$$$$$$$$$$$$$$$$$$$$$$");
  puts("      Tcache tear     ");
  puts("$$$$$$$$$$$$$$$$$$$$$$$");
  puts("  1. Malloc            ");
  puts("  2. Free              ");
  puts("  3. Info              ");
  puts("  4. Exit              ");
  puts("$$$$$$$$$$$$$$$$$$$$$$$");
  printf("Your choice :");
}


longlong read_int()
{
  longlong op;
  char local_28 [24];
  
  __read_chk(0,local_28, 23, 24);
  op = atoll(local_28);
  return op;
}


void add()
{
  ulong __size;
  uint uVar1;
  
  printf("Size:");
  __size = read_int();
  if (__size < 0x100) {
    g_ptr = malloc(__size);
    printf("Data:");
    uVar1 = __size - 0x10;
    _read(g_ptr, uVar1, uVar1);
    puts("Done !");
  }
}


void show(void)
{
  printf("Name :");
  write(1, &g_name, 0x20);
}

