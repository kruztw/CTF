// g_note 0x302080
// g_size 0x302060
// g_quata 0x302010 // 5

void main()
{
    alarm(0x3c);
    setvbuf(stdout,(char *)0x0,2,0);
    setvbuf(stdin,(char *)0x0,2,0);
    setvbuf(stderr,(char *)0x0,2,0);
    puts("----------BABYTCACHE----------");
    while(true){
        op = menu();
        switch(op) {
        default:
            puts("Invalid");
            break;
        
        case 1:
            add();
            break;
        
        case 2:
            edit();
            break;
        
        case 3:
            delete();
            break;
        
        case 4:
            show();
            break;
        
        case 5:
            exit(0);
    }
}


void menu()
{
  puts("1) Add note\n2) Edit note\n3) Free note\n4) View note\n5) Exit");
  printf(">> ");
  _read();
  return;
}


void _read()
{
  char local_38 [40];
  __read(local_38,0x20);
  atoi(local_38);
}


ulong __read(void *param_1,int param_2)
{
  int idx;
  ssize_t sVar2;
  
  sVar2 = read(0,param_1,(long)param_2);
  idx = (int)sVar2;
  if (idx == -1)
      exit(0);
  
  if (param_1[idx-1] == '\n')
      param_1[idx-1] = 0;
  
  return idx - 1;
}



void add()
{ 
    puts("Note index:");
    idx = _read();
    while( true ) {
        if(idx < 0 || idx > 7)
            return;

        if (g_note[idx]) {
            puts("This note is occupied\n");
            return;
        }
        puts("Note size:");
        size = _read();
        g_size[idx] = size;
        if (-1 < g_size[idx] && g_size[idx] < 0x201) break;
        puts("Invalid size");
    }

    g_note[idx] = malloc(g_size[idx]);
    if(!g_note[idx]) {
      puts("Note data:");
      __read(g_note[idx], g_size[idx]);
      return;
    }
    exit(0);
}


void edit()
{ 
    puts("Note index:");
    idx = _read();
    if (-1 < idx && idx < 8) { 
        if (!g_note[idx])
            puts("This Note is empty\n");
    
        else{
            puts("Please update the data:");
            idx = __read(g_note[idx], g_size[idx]);
            if (idx == 0)
                puts("update unsuccessful");
            else
                puts("update successful\n");
        }
    }
}


void delete()
{
    puts("Note index:");
    idx = _read();
    if (-1 < idx && idx < 8) {
        if (!g_note[idx])
            puts("This Note is empty");
        else {
            if(g_quata == 0) {
                g_quata --; // why??
                puts("Sorry no more removal\n");
                exit(0);
            }
        
        g_quata --;
        free(g_note[idx]); // uaf
        puts("done");
    }
  }
}


void show()
{  
    puts("Note index:");
    idx = _read();
    if (-1 < idx && idx < 8) { // bug idx == 7
        if(!g_note[idx])
            puts("This Note is empty");
        else
            printf("Your Note :%s\n\n", g_note[idx]);
    }
}

