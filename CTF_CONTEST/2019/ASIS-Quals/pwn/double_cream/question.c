void main()
{
  long canary;
  long in_FS_OFFSET;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
  foo1();
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();

  return 0;
}


void foo1()
{
  long canary;
  long in_FS_OFFSET;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  puts("hi all, please send me magics");
  foo2();

  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();
}


void foo2(void)
{
  long canary;
  long in_FS_OFFSET;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);

  printf("input 1: ");
  read(0,&DAT_00301060,0x400);

  printf("input 2: ");
  read(0,&DAT_00301460,0x400);

  printf(&DAT_00301060);
  printf(&DAT_00301460);
  
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();
}

