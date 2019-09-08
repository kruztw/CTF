// g_ptr  0x302060
// g_note 0x302080

void main()
{ 
  init();
  show_logo();
  
  while( true ) {
      op = show_and_read();
      switch(op){
        case 1:
          add();
          break;  

        case 2:
          delete();
          break;

        case 3:
          edit();
          break;

        case 4:
          exit(0);

        default:
          puts("invalid");
          break;
      }
  }
}



void init()
{ 
  puts("Loading......");
  sleep(4);
  setbuf(stdin,(char *)0x0);
  setbuf(stdout,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  alarm(0x3c);
}


void show_logo(void)
{
  puts("#     #    #     #####  ####### #######");
  puts("##    #   ##    #     #    #    #");
  puts("# #   #  # #    #          #    #");
  puts("#  #  #    #    #          #    #####");
  puts("#   # #    #    #          #    #");
  puts("#    ##    #    #     #    #    #");
  puts("#     #  #####   #####     #    #");
  puts("===========================================");
}


void show_and_read()
{
  puts("1.add.");
  puts("2.delete.");
  puts("3.modify.");
  puts("4.exit.");
  printf(">>");
  _read_();
}


void delete()
{ 
  printf("index:");
  idx = _read();
  if (idx < 0 || 9 < idx)
    puts("invalid");
  else {
    if(g_note[idx])
      g_ptr = g_note[idx];
    if (!g_ptr)
      puts("no such note!");
    else {
      free(g_ptr);
      g_note[idx] = NULL;
      puts("done!");
    }
  }
}



void _read_()
{
  char local_28 [24];
  _read(local_28, 16);
  atoi(local_28);
}


void _read(void *pvParm1,int len)
{
  read(0, pvParm1, len);
}



void add()
{
  for(int i = 0; i<10; i++)
      if(!g_note[i])
        break;

  if (i < 10) {
    g_note[i] = malloc(0x40);
    printf("content>>");
    _read(g_note[i], 0x40);
    puts("done!");
  }
  else
    puts("full!");
}


void edit()
{
  printf("index:");
  idx = _read_();
  g_ptr = g_note[idx];
  if (idx < 0 || 9 < idx || !g_ptr)
    puts("no such note!");
  else {
    printf("content>>");
    _read(g_ptr, 0x40);
    puts("done!");
  }
}