// g_table 0x0010404

struct message
{
    char topic[24];
    char *body;
    int body_size;
}; 

void main()
{ 
    initialize();
    puts("Welcome to messsage saving service.");
    puts("Please make a selection");
    menu();
    op = getint();
    switch(op) {
        default:
            puts("Invalid choice");
            break;

        case 1:
            add();
            break;

        case 2:
            edit();
            break;
        case 3:
            delete();
            break;
        case 4:
            view();
            break;
        case 5:
            exit(0);
    }
}


void initialize()
{
  alarm(0x3c);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin , 0, 2, 0);
}


void getint()
{
  char local_38 [40];
  getinp(local_38,0x20);
  atoi(local_38);
}


ulong getinp(void *_buf,int _len)
{
  len = read(0, _buf, _len - 1);
  _buf[len-1] = 0;
  return len - 1;
}




void add()
{ 
    puts("Enter the index");
    idx = getint();
    if (idx < 0 || 9 < idx)
        puts("Invalid index");
    else {
        ptr = malloc(0x28);
        puts("Enter the topic");
        getinp(ptr->topic, 0x18);
        puts("Enter the size of body");
        size = getint();
        if (size < 1 || 1000 < size)
            puts("The size entered is not valid");
        else {
            ptr->body_size = size;
            ptr->body = malloc(ptr->body_size);
            puts("Enter the body");
            getinp(ptr->body, ptr->body_size);
            g_table[idx] = ptr;
            puts("Message addition successfull");
        }
    }
}


void edit()
{ 
    puts("Enter the index");
    idx = getint();
    if (size < 0 || 9 < size || !g_table[idx])
        puts("Invalid index");
    else {
        ptr = g_table[idx];
        puts("Enter the new topic");
        getinp(ptr->topic, 0x18);
        puts("Enter the new body");
        getinp(ptr->body, ptr->body_size);
        puts("Message editing successfull");
    }
}


void delete()
{
    puts("Enter the index");
    idx = getint();
    if (idx < 0 || 9 < idx || g_table[idx])
        puts("Invalid index");
    else {
        ptr = g_table[idx];
        free(ptr->body);
        free(ptr);
        puts("Message deleting successfull");
        // 沒有將 g_table[idx] 設成 NULL
    }
}


void view()
{ 
    puts("Enter the index");
    idx = getint();
    if (idx < 0 || 9 < idx || !g_table[idx])
        puts("Invalid index");
    else {
        printf("Topic : ");
        puts(g_table[idx]->topic);
        printf("Body : ");
        puts(g_table[idx]->body);
        puts("Message viewing successfull");
    }
}

