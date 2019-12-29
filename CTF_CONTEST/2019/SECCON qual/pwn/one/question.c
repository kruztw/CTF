// g_memo 0x302050

void main()
{
    int op;
    printf("just one");
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
                show();
                break;

            case 3:
                delete();
                break;  

            default:
                puts("Wrong Input.");
                break;
        }

        puts("Done.");
    }
}

void menu()
{
  printf("\nMENU\n================\n1. Add\n2. Show\n3. Delete\n0. Exit\n================\n> ");
  getint();
}


void add()
{
  g_memo = malloc(0x40);
  if (!g_memo)
      puts("malloc failed...");
  else {
      printf("Input g_memo > ");
      getnline(g_memo, 0x40); //off by one
  }
}


void show()
{
  if (!g_memo)
      puts("Entry does not exist...");
  else
      puts(g_memo);
}


void delete()
{
    if (!g_memo)
        puts("Entry does not exist...");
    else
        free(g_memo);
}

