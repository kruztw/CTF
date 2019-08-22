void main()
{
  int iVar1;
  ssize_t sVar2;
  int in_GS_OFFSET;
  char local_1d;
  int fd;
  int local_18;
  int canary;
  undefined *local_c;
  
  local_c = &stack0x00000004;
  canary = *(int *)(in_GS_OFFSET + 0x14);
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
  alarm(0x3c);
  sleep(3);
  fd = open("/dev/urandom",0);

  if (read(fd, &local_1d, 1) != 1)
    _exit(-1);

  close(fd);

  local_18 = (int)local_1d;
  iVar1 = ((local_18 + 0x1eU) / 0x10) * -0x10;
  *(undefined4 *)(&stack0xffffffdc + iVar1) = 0x8048916;
  do_read();
  *(undefined4 *)(&stack0xffffffdc + iVar1) = 0x804891b;
  leave();
  if (canary != *(int *)(in_GS_OFFSET + 0x14)) {
    *(undefined4 *)(&stack0xffffffdc + iVar1) = 0x8048931;
    __stack_chk_fail();
  }

  return 0;
}


void do_read()
{
  int in_GS_OFFSET;
  void *ptr;
  int local_10;
  
  local_10 = *(int *)(in_GS_OFFSET + 0x14);
  ptr = NULL;
  puts("Which address you wanna read:");
  __isoc99_scanf("%u", &ptr);
  printf("%#x\n", *ptr);
  if (local_10 != *(int *)(in_GS_OFFSET + 0x14))
    __stack_chk_fail();
}


void leave()
{
  ssize_t sVar1;
  int in_GS_OFFSET;
  int i;
  char buf [160];
  undefined4 local_10;
  
  local_10 = *(undefined4 *)(in_GS_OFFSET + 0x14);
  memset(buf, 0, 0xa0);
  puts("Good Bye");
  i = 0;
  while (i < 0x9f) {
    if (read(0,buf + i, 1) != 1)
      exit(-1);

    if (buf[i] == '\n') break;
    i = i + 1;
  }

  printf(buf);
  _exit(0);
}

