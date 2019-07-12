int main()
{
  int result;
  void *b64ptr;
  char buf [30];
  uint len;
  
  memset(buf , 0, sizeof(buf));
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin , 0, 1, 0);

  printf("Authenticate : ");
  scanf("%30s", buf);

  memset(g_buf, 0, 12);
  b64ptr = NULL;
  len = Base64Decode(buf, &b64ptr);
  if (len < 13) {
      memcpy(g_buf, b64ptr, len);
      result = auth(len);
      if (result == 1) 
          correct();
  }
  else
      puts("Wrong Length");

  return 0;
}


uint auth(size_t len)
{
  char *result;
  char  local_18[8];
  char  tmp[8];
  
  memcpy(tmp, g_buf, len);
  result = calc_md5(local_18, 12);
  printf("hash : %s\n",result);
  return strcmp("f87cd601aa7fedca99018a8be88eda34", result);
}

