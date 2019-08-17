int main()
{
  undefined8 *puVar1;
  EVP_PKEY_CTX *ctx;
  uint op;
  char *name;
  char uStack36;
  undefined8 local_20;
  undefined8 local_18;
  
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 1, 0);

  fptr = (undefined8 *)malloc(40);
  fptr[3] = greetings;
  fptr[4] = byebye;

  printf("hey, what\'s your name? : ");
  scanf("%24s", name);
  puVar1 = fptr;
  *o = CONCAT44(uStack36,name);
  puVar1[1] = local_20;
  puVar1[2] = local_18;
  id = name;
  getchar();
  func[0] = echo1;
  func[1] = echo2;
  func[2] = echo3;
  
  while(1){
      puts("\n- select echo type -");
      puts("- 1. : echo1 echo");
      puts("- 2. : echo2 echo");
      puts("- 3. : echo3 echo");
      puts("- 4. : exit");
      printf("> ");
      ctx = (EVP_PKEY_CTX *)&DAT_00400c18;
      scanf("%d", &op);
      getchar();
    
      if(op < 3) 
          func[op-1]();
      else if(op == 4){
	  cleanup(ctx);
          printf("Are you sure you want to exit? (y/n)");
          op = getchar();
          if (op == 'y') break;
      }
      else
          puts("invalid menu");
  }

  puts("bye");
  return 0;
}


int greetings(char *_name)
{
  printf("hello %s\n", _name);
  return 0;
}


int byebye(char *_name)
{
  printf("goodbye %s\n", _name);
  return 0;
}


void get_input(char *_buf, int _len)
{
  fgets(_buf, _len, stdin);
  return;
}



int echo1()
{
  char buf [32];

  fptr[3];   //greetings
  get_input(buf, 128);
  puts(buf);
  fptr[4];   //byebye
  return 0;
}


int echo2(void)
{
  puts("not supported");
  return 0;
}


int echo3(void)
{
  puts("not supported");
  return 0;
}


void cleanup(EVP_PKEY_CTX *ctx)
{
  free(fptr);
  return;
}
