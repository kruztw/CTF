void main()
{
  char result;
  long in_FS_OFFSET;
  char pw [104];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  puts("plz enter password plz:");
  fgets(pw, 100, stdin);
  result = check(pw);
  if (result == 0)
    puts("lolno");
  else 
    puts("good job kthxbye");

  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();

  return 0;
}



int check(char *pw)
{
  int tmp;
  undefined8 rtn_value;
  
  tmp = rtn_value_p_1((ulong)pw[0]);
  if (tmp == 'e') {
    tmp = rtn_value_p_1((ulong)pw[1]);
    if (tmp == 'p') {
      tmp = rtn_value_p_1((ulong)pw[2]);
      if (tmp == 'h') {
        tmp = rtn_value_p_1((ulong)pw[3]);
        if (tmp == 'h') {
          tmp = rtn_value_p_1((ulong)pw[4]);
          if (tmp == 'z')
            rtn_value = 1;
          else
            rtn_value = 0;
        }
        else
          rtn_value = 0;
      }
      else 
        rtn_value = 0;
    }
    else 
      rtn_value = 0;
  }
  else 
    rtn_value = 0;

  return rtn_value;
}


ulong rtn_value_p_1(int value)
{
  return (ulong)(value + 1);
}

