// g_zfd  0x602120
// g_rfd  0x602124
// g_list 0x602140 // unit: 0x10
// g_lock 0x602170
// g_key  0x602190
// g_name 0x6021a0

g_list{
  int valid; 
  int id; // +4
  char *description // +8
}


void main()
{
    int op;

    puts(" _______  _______  _______  __   __  ______    _______    ___   _  _______  ___      _______ _______ \n|       ||       ||       ||  | |  ||    _ |  |       |  |   | | ||   _   ||   |   |       ||       |\n|  _____||    ___||       ||  | |  ||   | ||  |    ___|  |   |_| ||  |_| ||   |    |_     _||    ___|\n| |_____ |   |___ |       ||  |_|  ||   |_||_ |   |___   |     _||       ||   |      |   |  |   |___ \n|_____  ||    ___||      _||       ||    __  ||   ___|  |     |_ |       ||   |___   |   |  |    ___|\n _____| ||   |___ |     |_ |       ||  |  | ||   |___   |    _  ||   _   ||       |  |   |  |   |___\n|_______||_______||_______||_______||___|  |_||_______|  |___| |_||__| |__||_______|  |___| |_______|\n\n");

    printf("Input patient g_name... ");
    getnline(g_name, 64);
    puts("OK.");
    while( true ) {
        op = menu();
        switch(op){
            case 0:
                puts("Bye!");
                return 0;

            case 1:
                add();
                break;

            case 2:
                puts("No no no...\nThis is SECURE kalte.\nNo one can see entries. ( ´,_ゝ`)\n");
                break;

            case 3:
                delete();
                puts("Done.");
                break;

            case 4:
                modify();
                puts("Done.");
                break;

            case 99:
                edit name;  // ghidra沒顯示出來
                break;

            default:
                puts("Wrong rand.");
        }
    }
}


int init()
{
  setbuf(stdout, 0);
  g_zfd = open("/dev/zero", 0);
  g_rfd = open("/dev/urandom", 0);
  g_lock = getrand();
  g_key = g_lock;
}


void fini(void)
{
  if (zfd != -1)
    close(zfd);
  if (rfd != -1)
    close(rfd);
}


void menu()
{
  printf(        "\nMENU (patient : CENSORED)\n!#!#!#!#!#!#!#!#!#\n1.  Add\n2.  Show\n3.  Delete\n4. Modify\n99. Reg_name patient\n0.  Exit\n!#!#!#!#!#!#!#!#!#\n> "        );
  getint();
}


void add()
{
  int size;
  ulong __size;
  void *buf;
  uint i;
  uint rand;
  uint i;
  
  for(int i = 0; i<2; i++)
      if(list[i])
          break;

  if(i > 2){
      puts("karte is full!!");
      return;
  }

  printf("Input size > ");
  size = getint();
  __size = SEXT48(size);
  if (__size < 0x801)
     buf = calloc(1,__size);
  else
      buf = malloc(__size);

  if (buf == 0) {
    puts("alloction failed...");
    return;
  }

  if (0x800 < __size)
    read(g_zfd, buf, __size);
  
  printf("Input description > ");
  getnline(buf,__size);
  rand = getrand();
  for(int i = 0; i<3; i++)
    if (rand == list[i]+4 && list[i]) {
      rand = getrand();
      i = 0;
    }

  list[i] + 4 = rand;
  list[i] = 1;
  list[i] + 8 = buf;
  printf("\nAdded id %d\n",(ulong)rand);
}


undefined8 getrand(void)
{
  undefined8 local_18; 
  read(rfd, &local_18, 8);
  return local_18;
}


void getint()
{
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 rand;
  
  local_38 = 0;
  local_30 = 0;
  local_28 = 0;
  rand = 0;
  getnline(&local_38, 32);
  atoi(&local_38);
}


void delete()
{
  uint id;
  uint i;
  
  printf("Input id > ");
  id = getint();
  i = 0;
  while( true ) {
    if (i > 2){
      puts("karte not found...");
      return;
    }
    if (id == g_list[i]+4 && g_list[i]) break;
    i = i + 1;
  }
  g_list[i] = 0;
  free(g_list[i]+8);
  printf("\nDeleted id %d\n", id);
}


void modify()
{
  uint id;
  uint uVar2;
  size_t len;
  uint i;
  
  if (g_key == g_lock) {
    printf("Input id > ");
    id = getint();

    for(int i = 0; i<3; i++)
      if (id == g_list[i] + 4) {
        g_key = 0xdeadc0bebeef;
        printf("Input new description > ");
        len = strlen(g_list[i]+8) + 1;
        getnline(g_list[i]+8, len);
        printf("\nModified id %d\n", id);
        return;
      }

    puts("karte not found...");
  }
  else
    puts("Hey! You can\'t modify karte any more!!");
}