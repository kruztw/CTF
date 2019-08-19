void main()
{
  undefined local_11;
  undefined8 fd;
  
  setbuf(stdout,(char *)0x0);
  setbuf(stdin,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  printf("[#] number of bytes: ");
  fd = get_int();
  read(fd, &local_11, 100000);
  return 0;
}


undefined8 get_int(void)

{
  undefined8 fd;
  
  __isoc99_scanf(&DAT_00400c52, &fd);
  getchar();
  return fd;
}

