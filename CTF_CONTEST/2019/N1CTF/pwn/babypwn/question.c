struct member // 0x602060
{
  char name[0x10];
  char *description;
  int size;
}

void main()
{
  init();
  vuln();
  return 0;
}


void init()
{
  long lVar1;  
  setbuf(stdin,(char *)0x0);
  setbuf(stdout,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  alarm(0x5c);
}


void vuln()
{
  int op;
  
  puts("Welcome to N1CTF2019!");
  puts("Now that you are the leader of Nu1L Team.");
  puts("Do you wanna manage your team?");
  puts("Maybe you can do anything what you want..");
  while( true ) {
      menu();
      op = _read();
      switch(op){
        case 1:
          add();
          break;

        case 2:
          remove();
          break;    

        case 3:
          puts("Goodbye~");
          exit(0);

        default:  
          puts("Something Wrong..");
          break;
      }
  }
}


void menu()
{
  puts("======================\n");
  puts("1.Add a member");
  puts("2.Throw him out");
  puts("3.Exit\n");
  puts("======================");
  printf("Input your choice:");
}


void _read(void)
{
  char local_38 [40];
  
  read(0,local_38,4);
  atoi(local_38);
}


void remove()
{ 
  printf("index:");
  idx = _read();
  if (9 < idx) { // idx < 0 ?
    puts("invalid index!");
    exit(0);
  }
  free(member[idx]->description);
}


void add()
{ 
  for(int i = 0; i<10; i++)
    if(!member[i])
      break;

  if (i < 10) {
    member[i] = malloc(0x20);
    if(!member[idx]){
      puts("Malloc error!");
      exit(0);
    }

    printf("Member name:");
    read(0, member[idx], 0x10);
    printf("Description size:");
    size = _read();
    if (size < 0 || 0xff < size) {
      puts("It\'s tooooooooo large!");
      exit(0);
    }

    member[idx]->size = size;
    member[idx]->description = malloc(size);
    if(!member[idx] + 0x10){
      puts("Malloc error!");
      exit(0);
    }
    printf("Description:");
    read(0, member[idx]->description, size);
    puts("OK!");
  }
  else
    puts("Member is full!");
}

