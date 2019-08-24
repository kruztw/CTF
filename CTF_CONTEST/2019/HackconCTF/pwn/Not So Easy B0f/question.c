void main()
{
  long in_FS_OFFSET;
  undefined8 local_28;
  undefined8 local_20;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_28 = 0;
  local_20 = 0;

  printf("Enter name : ");
  fgets(&local_28, 0x10, stdin);
  puts("Hello");
  printf(&local_28);
  printf("Enter sentence : ");
  fgets(&local_28, 0x100, stdin);
  
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();

  return 0;
}

