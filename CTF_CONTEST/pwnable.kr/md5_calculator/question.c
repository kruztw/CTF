void main()
{
  int input;
  int hash_value;
  
  setvbuf(stdout,(char *)0x0,1,0);
  setvbuf(stdin,(char *)0x0,1,0);

  puts("- Welcome to the free MD5 calculating service -");
  srand(time(NULL));

  hash_value = my_hash();
  printf("Are you human? input captcha : %d\n",hash_value);
  scanf("%d",&input);
  if (hash_value != input) {
    puts("wrong captcha!");
    exit(0);
  }

  puts("Welcome! you are authenticated.");
  puts("Encode your data with BASE64 then paste me!");
  process_hash();
  puts("Thank you for using our service.");
  system("echo `date` >> log");
  return 0;
}


int my_hash()
{
  int rand;
  int in_GS_OFFSET;
  int i;
  int val[8];
  int canary;
  
  canary = *(int *)(in_GS_OFFSET + 0x14);
  i = 0;
  while (i < 8) {
    rand = rand();
    val[i] = rand;
    i = i + 1;
  }
  if (canary != *(int *)(in_GS_OFFSET + 0x14)) {
    __stack_chk_fail();
  }

  return val[1] + val[5] + (val[2] - val[3]) + val[7] + canary +(val[4] - val[6]);
}


void process_hash()
{
  undefined4 uVar1;
  void *__ptr;
  char *buf_ptr;
  int in_GS_OFFSET;
  char buf [512];
  int canary;
  
  canary = *(int *)(in_GS_OFFSET + 0x14);
  memset(buf, 0, sizeof(buf));
  memset(buf, 0, sizeof(g_buf));
  fgets(g_buf,0x400,stdin);

  uVar1 = Base64Decode(g_buf,buf);
  __ptr = (void *)calc_md5(buf,uVar1);
  printf("MD5(data) : %s\n",__ptr);
  free(__ptr);

  if (canary != *(int *)(in_GS_OFFSET + 0x14)) {
    __stack_chk_fail();
  }

  return;
}

