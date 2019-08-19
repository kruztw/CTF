// letters 0x0302050

void main()
{
  long in_FS_OFFSET;
  int op;
  int i;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  op = -1;
  setbuf(stdout, 0);
  setbuf(stdin, 0);
  setbuf(stderr, 0);
  
  i = 0;
  do {
    if (33 < i) {
        if (canary != *(long *)(in_FS_OFFSET + 0x28))
            __stack_chk_fail();
        return 0;
    }

    show_menu();
    scanf("%d", &op);
    switch(op){
        case 1:
            create_card();
            break;

        case 2:
            edit_card();
            break;

        case 3:
            discard();
            break;

        case 4:
            display();
            break;

        default:
            puts("omggg hacker");
            break;              
    }
    
    i = i + 1;
  } while( true );
}


void show_menu()
{
  puts("OPTIONS");
  puts("1) Create a postcard");
  puts("2) Edit a postcard");
  puts("3) Discard a postcard");
  puts("4) Read a postcard");
}


void edit_card()
{
  long in_FS_OFFSET;
  int idx;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  idx = 0;
  puts("Which envelope #?");
  scanf("%d", &idx);
  if (idx < 0 || 1 < idx)
    puts("swiper no swipey !");
  else {
    puts("Write.");
    read(0, letters[idx], 0x48);
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();
}


void create_card()
{
  int iVar1;
  void *pvVar2;
  long in_FS_OFFSET;
  int idx;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  idx = 0;
  puts("Which envelope #?");
  scanf("%d", &idx);
  iVar1 = idx;
  if (idx < 0)
    puts("swiper no swipey !");
  else {
      if (idx < 2)
          letters[ivar1] = malloc(0x48);
      else
          puts("u so greedy dat when u step on da scale, u see ur credit card number >:O");
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();
}


void discard()
{
  long in_FS_OFFSET;
  int idx;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  idx = 0;
  puts("Which envelope #?");
  scanf("%d", &idx);
  if (idx < 0 || 1 < idx)
    puts("swiper no swipey !");
  else
    free(letters[idx]);

  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();
}


void display()
{
  long in_FS_OFFSET;
  int i;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  idx = 0;
  puts("Which envelope #?");
  scanf("%d", &idx);
  if (idx < 0 || 1 < idx)
    puts("swiper no swipey !");
  else
    puts(letters[idx]);

  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();
}

