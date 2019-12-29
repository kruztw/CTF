// g_memo 0x302060

void main()
{
    printf("Remain");
    while(true){
        op = menu();
        switch(op){
            case 0:
                puts("Bye!");
                return 0;

            case 1:
                add();
                break;

            case 2:
                edit();
                break;

            case 3:
                delete();
                break;
        }
    puts("Done.");
    }
}


void add()
{ 
   ptr = malloc(0x48);
    if (!ptr)
        puts("malloc failed...");
    else {
        printf("Input g_memo > ");
        getnline(ptr,0x48);
        for(int i = 0; i<9; i++)
          if (!g_memo[i])
              break;

          if(i > 9){
              puts("g_memo is full!");
              free(ptr);
              exit(0);
          }
    }
    g_memo[i] = ptr;
}


void edit()
{ 
    printf("Input id > ");
    while( true ) {
        idx = getint();
        if (idx < 10) break;
        printf("Out of range!!\nInput id > ");
    }
    if (!g_memo[idx]) 
        puts("Entry does not exist...");
  
    else {
        printf("Input new g_memo > ");
        len = strlen(g_memo[idx]) + 1;
        getnline(g_memo[idx], len);
    }
}


void delete()
{
    printf("Input id > ");
    while( true ) {
        idx = getint();
        if (idx < 10) break;
        printf("Out of range!!\nInput id > ");
    }
    if (!g_memo[idx])
        puts("Entry does not exist...");
    else
        free(g_memo[idx]);
}

void getint()
{
    undefined8 local_98 [17] = {};
    getnline(local_98, 0x80); // bof
    atoi((char *)local_98);
}

