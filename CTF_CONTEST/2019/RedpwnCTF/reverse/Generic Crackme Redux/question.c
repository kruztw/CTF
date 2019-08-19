void main()
{
  char result;
  long in_FS_OFFSET;
  uint code;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Enter access code: ");
  scanf("%d", &code);
  result = check((ulong)code);

  if (result == 0)
    puts("Bzzzzrrrppp");
  else
    puts("Access granted");

  if (local_10 != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();

  return 0;
}


ulong check(int code)
{
  return (code * 10 == 705170);
}

