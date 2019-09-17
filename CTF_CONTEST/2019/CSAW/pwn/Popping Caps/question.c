void main()
{ 
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    printf("Here is system %p\n",system);

    i = 7;
    ptr = NULL;
    tmp = NULL;
    while (i != 0) {
        printf("You have %llu caps!\n",i);
        puts("[1] Malloc");
        puts("[2] Free");
        puts("[3] Write");
        puts("[4] Bye");
        puts("Your choice: ");
        op = read_num();
        
        switch(op){
            case 1:
                puts("How many: ");
                size = read_num();
                ptr = malloc(size);
                tmp = ptr;
                break;

            case 2:
                puts("Whats in a free: ");
                idx = read_num();
                free(ptr + idx);
                if (ptr == tmp)
                    tmp = NULL;
                break;

            case 3:
                puts("Read me in: ");
                read(0,tmp,8);
                break;

            case 4:
                bye()
                break;
        }
        
        puts("BANG!");
        i = i - 1;
    }

    bye();
    return 0;
}


void read_num()
{
  char local_38 [40];
  fgets(local_38, 32,stdin);
  atol(local_38);
}


void bye()
{
  fwrite("bye", 1, 4, stdout);
  malloc(0x38);
  exit(0);
}

    