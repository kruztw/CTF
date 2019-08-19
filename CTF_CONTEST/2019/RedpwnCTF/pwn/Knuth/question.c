void main()
{
  _end(stdout,(char *)0x0);
  _end(stdin,(char *)0x0);
  _end(stderr,(char *)0x0);
  usleep(300000);
  puts("[🔒] He \x1b[31m\x1b[1mprotec\x1b[0m");
  protec(); // heap rwx
  usleep(300000);
  puts("[\x1b[1mΩ\x1b[0m ] He \x1b[32m\x1b[1mTeX\x1b[0m");
  tex();
  usleep(300000);
  puts("But \x1b[1mmost\x1b[0m importantly");
  usleep(300000);
  puts("[💸] He \x1b[34m\x1b[1mchec\x1b[0m");
  usleep(300000);
  chec();
  return 0;
}


void tex(void)
{
  uint i;
  
  memset(art_of_computer_programming,0x5c,0x1000); 
  read(0,art_of_computer_programming,0x1000); // whole heap
  
  i = 0;
  while( true ) {
    if (0xfff < i)
      return;

    if ((((char)art_of_computer_programming[i] < ' ') ||
        (art_of_computer_programming[i] == 0x7f)) &&
       (art_of_computer_programming[i] != '\n')) break;
    i = i + 1;
  }

  __assert_fail("(s[i] >= 0x20 && s[i] < 0x7f) || s[i] == \'\\n\'","knuth.c",0x1e,
                (char *)&__PRETTY_FUNCTION__.2592);
}


void chec(void)
{
  int iVar1;
  
  iVar1 = __x86.get_pc_thunk.ax();
  (*(code *)(iVar1 + 0x3963))();
  return;
}

