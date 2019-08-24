void main()
{
  long in_FS_OFFSET;
  undefined8 input;
  undefined8 i;
  code *fptr;
  undefined8 local_38 [4];
  undefined8 local_18;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  alarm(0x1e);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);

  input = 0;       //rbp-0x50
  fptr = nope;     //rbp-0x40
  local_38[0] = 0; //rbp-0x30
  local_38[1] = 0; //rbp-0x28
  local_38[2] = 0; //rbp-0x20
  local_38[3] = 0; //rbp-0x18
  local_18 = 0;    //rbp-0x10
  i = 5; //rbp-0x48
  
  while (*(i+4) < 5) {
    fgets(&input, 0x11, stdin); // rbp-0x50
    strncpy(local_38[*(i+4)], &input, 8);
    *(i+4) ++;
  }

  *(i+4) = 0;
  
  while (*(i+4)_ < 5) {
    puts( local_38[*(i+4)] );
    *(i+4) ++;
  }

  (*fptr)(); // rbp-0x40
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();
}


void nope(void) // 0x400817
{
  puts("Naaa  , Try HArder");
  exit(1);
}


void win(void) // 0x400831
{
  puts("Yay , Here\'s the flag");
  system("cat ./flag.txt");
}