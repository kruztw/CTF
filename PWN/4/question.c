// g_flag 0x0302060

int main()
{
  code *__dest;
  long in_FS_OFFSET;
  undefined buf [264];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  init();
  read_flag();
  puts("Talk is cheap. Show me the shellcode.");
  read(0, buf, 0x100);
  __dest = (code *)mmap(0x0, 0x1000, 7, 0x22, -1, 0);
  memcpy(__dest, buf, 14);
  puts("Runing...");
  sendbox();
  (*__dest)();
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();
  
  return 0;
}


void init(void)

{
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stdin,(char *)0x0,2,0);
  setvbuf(stderr,(char *)0x0,2,0);
  return;
}


void read_flag(void)
{
  int __fd;
  
  __fd = open("/home/shellcode-2019/flag",0);
  if (__fd < 0) {
    puts("error");
    _exit(1);
  }
  read(__fd,&g_flag,0x100);
  close(__fd);
  return;
}


void sendbox(void)

{
  undefined8 uVar1;
  
  uVar1 = seccomp_init(0);
  seccomp_load(uVar1);
  return;
}

