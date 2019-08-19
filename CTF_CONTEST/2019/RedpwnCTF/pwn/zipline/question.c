void main(void)
{
  undefined *puVar1;
  
  puVar1 = &stack0x00000004;
  setbuf(stdout,(char *)0x0);
  setbuf(stdin,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  puts("Ready for a ride on the zipline to hell?");
  zipline(puVar1);
  i_got_u();
  return 0;
}


void zipline(void)
{
  char local_16 [14];
  
  __x86.get_pc_thunk.ax();
  gets(local_16);
  return;
}

a = 0x0804c040

void i_got_u(void)
{
  char local_79 [101];
  ssize_t local_14;
  int local_10;
  
  if (((((a == 0) || (b == 0)) || (c == 0)) || ((d == 0 || (e == 0)))) ||
     ((f == 0 || ((g == 0 || (h == 0)))))) {
    return;
  }

  local_10 = open("flag.txt",0);
  if (local_10 == -1) {
    puts("Error opening flag, tell organizer");
    perror("opening flag:");
    exit(1);
  }
  local_14 = read(local_10,local_79,100);
  if (local_14 == -1) {
    puts("Error reading flag, tell organizer");
    perror("reading flag:");
    exit(1);
  }
  local_79[local_14] = 0;
  puts(local_79);
  close(local_10);
  exit(0);
}

