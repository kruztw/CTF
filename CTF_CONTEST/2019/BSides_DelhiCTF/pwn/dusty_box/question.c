// g_header 0x104060
// g_table 0x104080

struct session
{
	short cookie;
	char *content;  // +0x2 (? 0x8)
	void *fptr; // +0x10
	session *next; // +0x18
};

void main()
{
  	initialize();
    while( true ) {
        menu();
        op = getInt();
        switch(op){
        	case 1:
        		Store();
        		break;
        	case 2:
        		LOAD();
        		break;
        	case 3:
        		Remove();
        		break;
        	case 4:
        		Restore(g_header+0x8);
        		break;
        }
   	}
}



void initialize()
{ 
  	srand(time(NULL));
  	setvbuf(stdout, 0, 2, 0);
  	setvbuf(stderr, 0, 2, 0);
  	setvbuf(stdin, 0, 2, 0);
  	g_header = g_table;
}


void menu()
{
  	puts("1 : New Session");
  	puts("2 : Load Session");
  	puts("3 : Remove Session");
  	puts("4 : Restore Session");
  	printf(">> ");
}


void getInt()
{
  	char local_38[40];
  	Read(local_38, 20);
  	atol(local_38);
}

long getId()
{ 
  	printf("Enter the Id : ");
  	id = getInt();
  	if (id < 0)
    	exit(1);

	  return id;
}


long Read(void *_buf,long _len)
{ 
  	len = read(0, _buf, _len - 1);
  	if (len < 0)
    	exit(0);

  	_buf[len - 1] = 0;
  	return len - 1;
}


void Load()
{ 
  	id = getId() % 11;
  	cookie = getCookie();
  	ptr = g_table[id];
  
  	if(ptr){
 		if (cookie == ptr->cookie){
    	  	g_header+0x8 = g_table[id];
      		g_table[id] = ptr->next;
      		display(ptr->content);
      		return;
    	}
    	if (ptr->next) {
      		while (cookie != ptr->next->cookie && ptr->next->next)
        		ptr = ptr->next;
      
      		if (cookie == ptr->next->cookie) {
        		g_header+0x8 = ptr->next;
        		ptr->next = ptr->next->next;
        		display(ptr->content);
        		return;
      		}
    	}
  	}
  	puts("Session not Found!");
}


void Remove()
{ 
  	id = getId();
  	cookie = getCookie();
  	ptr = g_header+0x8;
  	if (g_header+0x8 && cookie == (g_header+0x8)->cookie) {
    	g_header+0x8 = NULL;
    	free(ptr->content);
    	free(ptr);
    	return;
  	}
  	ptr = g_table[id%11];
  	if(!ptr)
  		puts("Invalid Id");
  	else {
    	if(cookie == ptr->cookie) {
      		g_table[id%11] = ptr->next;
      		free(ptr + 2);
      		free(ptr);
      		return;
    	}
    	if (ptr->next){
      		while (cookie != ptr->next->cookie &&  ptr->next->next)
	        	ptr = ptr->next;
    	  	if (cookie == ptr->next->cookie) {
        		free(ptr->next->content);
        		free(ptr->next);
	        	ptr->next = ptr->next->next;
    	    	return;
      		}
    	}
  	}
  	exit(1);
}


void getCookie()
{
  	printf("Enter Cookie : ");
  	getInt();
}


void Restore(long lParm1,undefined8 _ptr)
{
  	if (lParm1 == 0)
    	puts("No session to restore");
  	else
		(_ptr->fptr)(_ptr->content);
}


void Store()
{
  	id = getId();
  	content = Malloc(0x20);
  	printf("Content : ");
  	Read(content, 0x20);
  	Insert(id, content);
}


void * Malloc(size_t _size)
{ 
  	s = malloc(_size);
  	if (!s) {
    	perror("malloc");
    	exit(1);
  	}
  	memset(s, 0, _size);
  	return s;
}



void Insert(int _id, undefined8 _ptr)
{ 
  	ptr = Malloc(0x20);
  	ptr->content = _ptr;
  	ptr->cookie = rand();
  	ptr->fptr = &restore;
  	ptr->next = NULL;
  	_id = _id % 11;
  	if (!table[_id]) 
    	table[_id] = ptr;
  	else {
    	tmp = table[_id];
    	fwhile (tmp->next)
      		tmp = tmp->next;

    	tmp->next = ptr;
  	}
  	printf("Cookie : %x\n", ptr->cookie);
}


void restore()
{
  puts("TODO : restores the current session");
  return;
}



void display(undefined8 uParm1)
{
  printf("Content : ");
  write(uParm1, 32);
  putchar('\n');
}

