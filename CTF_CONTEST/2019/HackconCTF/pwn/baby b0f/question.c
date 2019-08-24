void main()
{
  undefined8 local_16;
  undefined2 local_e;
  int local_c;
  
  alarm(0x1e);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
  local_c = -0x35014542;
  local_16 = 0;
  local_e = 0;
  fgets((char *)&local_16,0x100,stdin);
  if (local_c == -0x21524111)
    system("cat ./flag.txt");
  else
    puts("Try Again");

  return 0;
}

