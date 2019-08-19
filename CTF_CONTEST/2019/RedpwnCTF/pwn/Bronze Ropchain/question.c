void main()
{
  char buffer [1024];
  undefined *local_10;
  
  local_10 = &stack0x00000004;
  setbuf((FILE *)stdout,(char *)0x0);
  setbuf((FILE *)stdin,(char *)0x0);
  setbuf((FILE *)stderr,(char *)0x0);
  puts("What is your name?");
  fgets(buffer,0x400, stdin);
  greet(buffer);
  return 0;
}


void greet(char *param_1)
{
  char local_1c [20];
  
  strcpy(local_1c,param_1);
  printf("Hello %s! How are you on this fine day?\n",local_1c);
  getchar();
  return;
}

