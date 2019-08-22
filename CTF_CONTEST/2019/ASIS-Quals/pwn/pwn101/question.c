// g_phone   0x0302040
// g_addr    0x0302048
// g_descrip 0x0302050

void main()
{
  int op;
  
  init();
  while(true){
    op = menu();
  	switch(op){
  		case 1:
     	   	add();
     	   	break;

     	case 2:
      		show();
      		break;

      	case 3:
    		delete();
    		break;

  	}
  }

  puts("Bye.");
  return 0;
}


void init()
{
  setvbuf(stdout, 0, 2, 0);
  signal(0xe, FUN_001009b0);
  alarm(0x3c);
  return;
}


ulong menu(void)
{
  long in_FS_OFFSET;
  uint op;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  puts("++++++++++++++++++++++++");
  puts(" 1) Add an address");
  puts(" 2) Show an address");
  puts(" 3) Delete an address");
  puts("++++++++++++++++++++++++");
  printf("> ");
  scanf("%d", &op);
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();

  return op;
}


void add()
{
  void *ptr;
  long in_FS_OFFSET;
  int len;
  uint op;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);

  for(int i = 0; i<10; i++)
  	if(!g_addr[i])
  		break;

  if (i == 10)
  		puts("You can\'t add any more addresses.");
  else {
    printf("Description Length: ");
    scanf("%d", &len);
    if (len < 0 || 0x2000 < len)
      puts("Invalid size.");
    else {
      ptr = malloc(0x20);
	  g_addr[i] = ptr;
      ptr = malloc(len);
      g_descrip[i] = ptr;
      len = len + 1;  // bug !!!!!!
      printf("Phone Number: ");
      scanf("%d", &g_phone[i]);
      printf("Name: ");
      read(0, &g_addr[i], 0x20);
      printf("Description: ");
      read(0, &g_descrip[i], len);
      printf("Added an address: index=%d\n", i);
    }
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
  	__stack_chk_fail();
}


void show()
{
  long in_FS_OFFSET;
  int idx;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  printf("Index: ");
  scanf("%d",&idx);
  if (idx < 0 || 9 < idx)
    puts("Invalid index.");
  else {
    if (!g_addr[idx])
      puts("Unused address.");
    else {
      printf("Phone Number: %d\n", g_phone[idx]);
      printf("Name        : %s\n", g_addr[idx]);
      printf("Description : %s\n", g_descrip[idx]);
    }
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();
}


void delete(void)
{
  long in_FS_OFFSET;
  int idx;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  printf("Index: ");
  scanf("%d", &idx);
  if (idx < 0 || 9 < idx)
    puts("Invalid index.");
  else {
    if (!g_addr[idx])
      puts("Unused address.");
    else {
      free(g_addr[idx]);
      free(g_descrip[idx]);
      g_phone[idx] = 0;
      g_addr[idx] = 0;
      g_descrip[idx] = 0;
      puts("OK.");
    }
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();
}