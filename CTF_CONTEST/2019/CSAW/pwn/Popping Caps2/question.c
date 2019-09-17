void main()
{ 
    setvbuf(stdout,(char *)0x0,2,0);
    setvbuf(stdin,(char *)0x0,2,0);
    setvbuf(stderr,(char *)0x0,2,0);
    
    printf("Here is system %p\n",system);
    i = 7;
    ptr = (void *)0x0;
    tmp = (void *)0x0;
    
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
                __size = read_num();
                ptr = malloc(__size);
                tmp = ptr;      
                break;

            case 2:
                puts("Whats in a free: ");
                lVar2 = read_num();
                free((void *)((long)ptr + lVar2));
                if (ptr == tmp)
                    tmp = (void *)0x0;
                break;

            case 3:
                puts("Read me in: ");
                read(0,tmp,0xff);
                break;

            case 4:
                bye();
        }

        puts("BANG!");
        i = i - 1;
    }
    
    bye();
    return 0;
}


void read_num(void)
{
  char local_38 [40];
  long local_10;
  
  fgets(local_38, 32,stdin);
  atol(local_38);
}




void bye()
{
  exit(0);
}

