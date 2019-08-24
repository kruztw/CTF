int entry()
{
  main();
  syscall();
  syscall();
  syscall();
  return CONCAT88(0xa0,1);
}


int main()
{
  syscall();
  syscall();
  return CONCAT88(0xa0,1);
}

