void main(void)
{
    undefined8 addr;
    undefined8 op;
  
    addr = mmap_chunk();
    while(true){
        menu();
        op = _read();
        switch(op){
            case 1:
                alloc(addr);
                break;
            case 2:
                Fill(addr);
                break;
            case 3:
                Free(addr);
                break;
            case 4:
                Dump(addr);
                break;

            case 5:
                exit(0);
        }
    }

    return 0;
}


long mmap_chunk(void)
{
  int fd;
  ssize_t len;
  void *addr;
  void *pvVar2;
  long in_FS_OFFSET;
  ulong local_28;
  ulong i;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
  alarm(0x3c);

  puts("===== Baby Heap in 2017 =====");
  
  if ( (fd = open("/dev/urandom",0)) > -1 ) {
    if (read(fd, &local_28, 16) == 0x10) {
      close(fd);
      addr = (void *)(local_28 % 0x555555543000 + 0x10000 & 0xfffff000);
      if (mmap(addr,0x1000,3,0x22,-1,0) != addr)
        exit(-1);
      if (canary != *(long *)(in_FS_OFFSET + 0x28))
        __stack_chk_fail();

      return (i + SUB168(ZEXT816(i >> 7) * ZEXT816(0x8d3dcb08d3dcb0d) >> 0x40,0) * -0xe80 & 0xfffffffffffffff0) + (long)addr;
    }
  }

  exit(-1);
}


void menu()
{
  puts("1. Allocate");
  puts("2. Fill");
  puts("3. Free");
  puts("4. Dump");
  puts("5. Exit");
  printf("Command: ");
}


void _read(void)
{
  long in_FS_OFFSET;
  char i [8];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  FUN_0010123d(i,8);
  atol(i);
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();
}

ulong FUN_0010123d(long lParm1,long lParm2)
{
  int *pidx;
  ulong rtn_value;
  long in_FS_OFFSET;
  char local_21;
  ulong i;
  ssize_t i;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  if (lParm2 == 0)
    rtn_value = 0;
  else {
    i = 0;
    do {
      while( true ) {
        if (lParm2 - 1U <= i) goto LAB_001012e7;
        if (read(0, &local_21, 1) < 1) break;
        if (local_21 == '\n') goto LAB_001012e7;
        lParm1[i] = local_21;
        i = i + 1;
      }
      pidx = __errno_location();
    } while ((*pidx == 0xb) || (pidx = __errno_location(), *pidx == 4));
LAB_001012e7:
    lParm1[i] = 0;
    rtn_value = i;
  }

  if (canary == *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();

  return rtn_value;
}



void alloc(long lParm1)
{
  void *ptr;
  uint i;
  int size;
  
  i = 0;
  while( true ) {
    if (15 < i)
      return;
    if (!lParm1[i]) break;
    i = i + 1;
  }
  printf("Size: ");
  size = _read();
  if (size < 1)
    return;

  if (0x1000 < size)
    size = 0x1000;
  ptr = calloc(size, 1);
  if (ptr) {
    lParm1[i] = 1;
    lParm1[i] + 8 = size;
    lParm1[i] + 0x10 = ptr;
    printf("Allocate Index %d\n", i);
    return;
  }

  exit(-1);
}


void Fill(long lParm1)
{
  int idx;
  int size;
  
  printf("Index: ");
  idx = _read();
  if (((-1 < idx) && (idx < 16)) && lParm1[idx] == 1) {
    printf("Size: ");
    size = _read();
    // heap overflow , if size > content size
    if (0 < size) {
      printf("Content: ");
      _write_content(lParm1[idx] + 0x10, size);
    }
  }
}


ulong _write_content(long lParm1,ulong uParm2)
{
  ssize_t len;
  int *psize;
  ulong rtn_value;
  
  if (uParm2 == 0)
      return 0;
  else {
    rtn_value = 0;
    do {
      while( true ) {
        if (uParm2 <= rtn_value)
          return rtn_value;
        if (read(0, lParm1 + rtn_value, uParm2 - rtn_value) < 1) break;
        rtn_value = rtn_value + len;
      }
      psize = __errno_location();
    } while ((*psize == 0xb) || (psize = __errno_location(), *psize == 4));
  }
  return rtn_value;
}



void Free(long lParm1)
{
  int idx;
  
  printf("Index: ");
  idx = _read();
  if (((-1 < idx) && (idx < 0x10)) && lParm1[idx] == 1){
    lParm1[idx] = 0;
    lParm1[idx] + 8 = 0;
    free(lParm1[idx] + 0x10);
    lParm1[idx] + 0x10 = 0;
  }
}

void Dump(long lParm1)
{
  undefined8 addr;
  int size;
  
  printf("Index: ");
  idx = _read();
  if (-1 < idx && idx < 0x10 && lParm1[idx] == 1){
    puts("Content: ");
    _write(lParm1[idx] + 0x10, lParm1[idx] + 8);
    puts("");
  }
}


ulong _write(long lParm1,ulong uParm2)
{
  ssize_t len;
  int *piVar2;
  ulong local_18;
  
  local_18 = 0;
  do {
    while( true ) {
      if (uParm2 <= local_18) {
        return local_18;
      }
      len = write(1,(void *)(lParm1 + local_18),uParm2 - local_18);
      if (len < 1) break;
      local_18 = local_18 + len;
    }
    piVar2 = __errno_location();
  } while ((*piVar2 == 0xb) || (piVar2 = __errno_location(), *piVar2 == 4));
  return local_18;
}

