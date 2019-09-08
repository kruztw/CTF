// g_valid      0x302014
// g_fd_urandom 0x302018
// g_mmap_addr  0x302020

void main()
{
  	undefined buf[64]; //rbp-0x60
  	int random;       // rbp-0x20
  	char op[16];     //  rbp-0x10       
  
  	init();
  	g_fd_urandom = open("/dev/urandom",0);
  	read(g_fd_urandom, &random, 16);
  	ptr = g_mmap_addr;
  	*g_mmap_addr = random;
  	*(ptr+8) = local_20;
  	close(g_fd_urandom);

  	while( true ) {
    	write(1, '>> ', 3);
	    __read_chk(0, op, 16);
    	switch(op[0]){
    		case '1':
    			  if (g_valid == 0)
          			check(&random);
        		else
          			g_valid = 0;
          	break;

    		case '2':
    			return;

    		case '3':
    			if (g_valid == 0)
        			puts("Ing_valid choice");
      			else
        			vuln(buf);

        		break;

        	default:
        		puts("Ing_valid choice");
      	}
    }
	if (g_valid == 0)
  		exit(0);

  	iVar2 = memcmp(&random, g_map_addr, 16);
  	if (iVar2 != 0)
    	__stack_chk_fail();

  	return 0;
}


void init()
{
  signal(0xe,FUN_00100d0f);
  alarm(0x708);
  g_mmap_addr = mmap((void *)0x0,0x1000,3,0x22,-1,0);
  if (g_mmap_addr == (void *)0xffffffffffffffff) {
    puts("mmap error");
    exit(0);
  }
  setvbuf(stdin,(char *)0x0,2,0);
  setvbuf(stdout,(char *)0x0,2,0);
}




void vuln(char *_target)
{
  char buf[128];
  printf("Copy :");
  _read(buf, 63);
  strcpy(_target, buf); // bof
  puts("It is magic copy !");
}


void check(char *_real_pw) 
{
  char pw [128];
  
  printf("Your passowrd :");
  _read(pw, 127);
  len = strlen(pw);
  if (strncmp(pw, _real_pw, len) == 0) {
    g_valid = 1;
    puts("Login Success !");
  }
  else
    puts("Failed !");
}


void _read(void *_buf,uint _len)
{
	read_len = read(0,_buf, _len);
  	if(read_len < 1) {
    	puts("read error");
    	_exit(1);
  	}
  	if (_buf[read_len-1] == '\n') {
    	_buf[read_len-1] = 0;
  	}
}