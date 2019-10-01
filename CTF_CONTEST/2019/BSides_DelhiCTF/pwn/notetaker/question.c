// g_table  0x6020a0
// g_size   0x602100

struct note
{
    char title[0x20];
    char *description; //0x20
    int des_size; //0x28

};

void main()
{ 
    initialise();
    while( true ) {
        op = menu();
        switch(op){
            case 1:
                add();
                break;
            
            case 2:
                edit();
                break;

            case 3:
                show();
                break;

            default:
                puts("Invalid!");
                break;
        }
    }
}


void initialise()
{
  setvbuf(stdin , 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
}


void menu()
{
  puts("1. Add note");
  puts("2. Edit note");
  puts("3. Show note");
  puts("4. Delete note");
  printf("Your Choice > ");
  getint();
}


void getint()
{
  char local_38 [40];
  getinp(local_38, 20);
  atoi(local_38);
}


ulong getinp(char *_buf,int _len)
{ 
  len = read(0, _buf, _len - 1);
  if(len < 0)
      exit(0);

  _buf[len-1] = 0; // one_byte overwrite
  return len - 1;
}


void add()
{ 
    i = 0;
    while (i < 13 && g_table[i]) //bug i 可能等於 13 但最多只能容納 12 個 note
        i = i + 1;

    if (i != 12) {  // != ???
        printf("Enter size: ");
        size = getint();
        if(0 < size && size < 0x1e) {
            ptr = malloc(0x30);
        
            printf("Enter title: ");
            getinp(ptr->title, size);
            printf("Enter desc size: ");
            des_size = getint();
            if (des_size < 0x3e9) {
                ptr->description = malloc(des_size);
                printf("Enter desc: ");
                getinp(ptr->description, des_size);
                ptr->des_size = des_size;
                g_table[i] = ptr;
                g_size[i] = size;
            }
            puts("Whoa, your RAM might be huge, mine ain\'t!");
            exit(0);
        }
        puts("Lol, can\'t give such a simple bof!");
        exit(0);
    }   
    puts("Outta space dude!");
    exit(0);
}


void edit()
{
    printf("Enter index: ");
    idx = getint();
    if (-1 < idx && idx < 12) {
        ptr = g_table[idx];
        printf("Enter title: ");
        getinp(ptr->title, g_size[idx]);
        printf("Enter desc: ");
        getinp(ptr->description, ptr->des_size);
        return;
  }

  exit(0);
}


void show()
{
  puts("Whoops! Well lets just say you need to look somewhere else for a leak!");
}


void delete()
{ 
    printf("Enter index: ");
    idx = getint();
    if (-1 < idx && idx < 12) {
        ptr = g_table[idx];
        free(ptr->description);
        free(ptr);
        g_table[idx] = NULL;
        g_size[idx] = 0;
        // 沒有把 description 設成 NULL 
    }

    exit(0);
}

