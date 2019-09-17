// tIndex 0x6020bc
// trips  0x6020c0

struct trip
{
    char *destination;
    int distance;    
};

int main(int argc)
{ 
    local_1c = argc;
    puts("\nHello! Welcome to trip management system. ");
    printf("%p \n", &local_1c);
    puts("\nChoose an option: ");

    while( true ) {
        puts("\n1. Add a trip ");
        puts("2. Change a trip ");
        puts("3. Delete a trip ");
        puts("4. Check a trip ");
        printf("> ");
        fflush(stdout);
        fgets(choice, 4, stdin);
        op = atoi(choice);
        switch(op){
            case 1:
                add();
                break;
            case 2:
                change();
                break;
            case 3:
                delete();
                break;

            case 4:
                show();
                break;
        }
    }
}


void change()
{
  char buf [20];
  
  printf("Update trip: ");
  fgets(buf, 20, stdin);
  idx = strtoul(buf, 0, 0);
  if (idx < tIndex) { // idx < 0 ?
    len = read(0, trips[idx]->destination, trips[idx]->distance);
    trips[idx]->destination[len] = 0;
  }
  else
    puts("No upcoming trip to update.");
}


void delete()
{
  char buf [20];
  
  printf("Which trip you want to delete: ");
  fgets(buf, 20, stdin);
  idx = strtoul(buf, 0, 0);
  if (idx < tIndex) {
      if (0 < tIndex) {
          trips[idx] = trips[tIndex - 1];
          tIndex = tIndex - 1;
      }
      free(trips[idx]->destination);
      free(trips[idx]);
  }
  else
      puts("That trip is not there already.");
}



void show()
{
  char choice [4];
  
  puts("Which trip you want to view? ");
  putchar('>');
  fgets(choice, 4, stdin);

  idx = strtoul(choice, 0, 0);
  if (idx < tIndex)
      printf("%s \n",trips[idx]->destination);
  else
      puts("No trip in here. ");
}


void add()
{

    char choice [4];
  
    if(tIndex != 7) {
        puts("Adding new trips...");
        ptr = (trip *)malloc(0x10);
        puts("Choose a Distance: ");
        puts("1. 0x80 ");
        puts("2. 0x110 ");
        puts("3. 0x128 ");
        puts("4. 0x150 ");
        puts("5. 0x200 ");
        printf("> ");
        fgets(choice, 4, stdin);
        op = atoi(choice);
        switch(op) {
            default:
                puts("Can\'t you count?");
                return;
            
            case 1:
                ptr->distance = strtoul("0x80", 0, 0);
                ptr->destination = (char *)malloc(ptr->distance);
                printf("Destination: ");
                fgets(ptr->destination, ptr->distance, stdin);
                break;
            
            case 2:
                uVar3 = strtoul("0x110", 0, 0);
                ptr->distance = uVar3;
                pcVar4 = (char *)malloc(ptr->distance);
                ptr->destination = pcVar4;
                printf("Destination: ");
                fgets(ptr->destination,(int)ptr->distance,stdin);
                break;
            case 3:
                uVar3 = strtoul("0x128",(char **)0x0,0);
                ptr->distance = uVar3;
                pcVar4 = (char *)malloc(ptr->distance);
                ptr->destination = pcVar4;
                printf("Destination: ");
                fgets(ptr->destination,(int)ptr->distance,stdin);
                break;
            case 4:
                uVar3 = strtoul("0x150",(char **)0x0,0);
                ptr->distance = uVar3;
                pcVar4 = (char *)malloc(ptr->distance);
                ptr->destination = pcVar4;
                printf("Destination: ");
                fgets(ptr->destination,(int)ptr->distance,stdin);
                break;
            case 5:
                uVar3 = strtoul("0x200",(char **)0x0,0);
                ptr->distance = uVar3;
                pcVar4 = (char *)malloc(ptr->distance);
                ptr->destination = pcVar4;
                printf("Destination: ");
                fgets(ptr->destination,(int)ptr->distance,stdin);
        }

        printf("Trip %lu added.\n", tIndex);
        tmp = tIndex;
        tIndex = tIndex + 1;
        trips[tmp] = ptr;
        return;
    }

    puts("Cannot add more trips.");
    exit(0);
}