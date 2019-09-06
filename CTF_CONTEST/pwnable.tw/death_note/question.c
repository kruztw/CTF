void main()
{
  int op;
  
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);

	while( true ) {
 		menu();
    	op = read_int();
    	switch(op){
    		case 1:
	    		add_note();
    			break;

    		case 2:
    			show_note();
	    		break;

    		case 3:
    			del_note();
    			break;

    		case 4:
    			exit(0);
	    		break;

    		default:
    			puts("Invalid choice");
    			break;
    	}
    }
}


int read_int()
{
  ssize_t len;
  int op;
  char buf[16];
  
  len = read(0, buf, 15);
  if (len < 1) {
    puts("read error");
    exit(1);
  }

  op = atoi(buf);
  return op;
}


void menu()
{
  puts("-----------------------------------");
  puts("             DeathNote             ");
  puts("-----------------------------------");
  puts(" 1. Add a name                     ");
  puts(" 2. show a name on the note        ");
  puts(" 3. delete a name int the note     ");
  puts(" 4. Exit                           ");
  puts("-----------------------------------");
  printf("Your choice :");
}


void show_note()
{
  int idx;
  
  printf("Index :");
  idx = read_int();
  if (10 < idx) {  // idx < 0  can leak something.
    puts("Out of bound !!");
    exit(0);
  }

  if (note[idx])
    printf("Name : %s\n", note[op]);
}


void add_note()
{
  int op;
  char *pcVar3;
  char buf[80];
  
  printf("Index :");
  op = read_int();
  if (10 < op) { // idx < 0 can write got
    puts("Out of bound !!");
    exit(0);
  }

  printf("Name :");
  read_input(buf, 80);
  if (is_printable(buf)) {
    note[idx] = strdup(buf);
    puts("Done !");
    return;
  }
  puts("It must be a printable name !");
}


void del_note()
{
  int op;
  
  printf("Index :");
  op = read_int();
  if (10 < op) {
    puts("Out of bound !!");
    exit(0);
  }
  free(note[op]);
  note[op] = NULL;
}


bool is_printable(char *_buf)
{
	for(int i = 0; i<strlen(_buf); i++) 
    	if (_buf[i] < ' ' || _buf[i] == 0x7f)
    		return 0;
  return 1;
}

