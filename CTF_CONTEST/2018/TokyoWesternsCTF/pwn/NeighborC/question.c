void main()
{
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
  sleep(3);
  FUN_00100937();
  exit(0);
}


void FUN_00100937(void)
{
  puts("Hello neighbor!");
  puts("Please tell me about yourself. I must talk about you to our mayor.");
  FUN_001008d0(stderr);
}


void FUN_001008d0(FILE *pFParm1)
{
  char *pcVar1;
  
  while( true ) {
    if(!fgets(&DAT_00301060, 0x100, stdin)) break;
    fprintf(pFParm1, &DAT_00301060);
    sleep(1);
  }
  _exit(1);
}