void main()
{
  long in_FS_OFFSET;
  char num;
  char local_121;
  double result;
  double digit [33];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  result = 0.00000000;
  init();
  puts("+++++++++++++++++++++++++++++++++++++");
  puts("+++++ Online Median Calculator ++++++");
  puts("+++++++++++++++++++++++++++++++++++++");
  printf("Number of values: ");
  scanf("%hhd", &num);
  for(int i = 0; i<num; i++)
  		__isoc99_scanf("%lf", digit[i]);

  for(int i = 0; i<num; i++)
    	result = digit[i] + result;

  result /= num;
  printf((char *)ZEXT816((ulong)result),"Result = %f\n");
  if (canary != *(long *)(in_FS_OFFSET + 0x28))
    __stack_chk_fail();

  return 0;
}


void init()
{
  setvbuf(stdout, 0, 2, 0);
  signal(0xe,FUN_00400766);
  alarm(0x3c);
}

