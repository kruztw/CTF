// g_table 0x6020c0
// g_data  0x602120

struct account
{
	char username[20];
	int addr_size;
	char *addr;
	int money;
};

struct hash
{
	int uhash;
	int phash;
}

void main()
{ 
  	initialize();
    while( true ) {
    	puts("\tManage your money");
    	puts("\t1. REGISTER");
    	puts("\t2. LOGIN");
    	puts("\t3. EXIT");
    	printf("Enter your choice :");
    	scanf("%d", &op);
    	if (op == 1)
    		register_user();
    	else if(op == 2)
    		login();
 	 }

  	exit(0);
}


void initialize()
{
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
}


void register_user()
{
  	char password[24];
    
  	i = 0;
  	size = 0;
  	idx = 0;
  	while (i < 10 && g_table[i])
    	i = i + 1;
  
  	if (9 < i) {
    	puts("FULL");
    	exit(0);
  	}

  	idx = i;
  	puts("----Registeration Desk----");
  	ptr = (char *)malloc(0x30);
  	printf("Enter your new username :");
  	get_inp(ptr->username, 20);
  
  	i = 0;
  	while (i < 10) {
    	if(g_data[i])
      		if (!strncmp(ptr->username, g_data[i]->username, 20)) {
        		puts("Username taken");
        		exit(0);
      		}
    	i = i + 1;
  	}
  	
  	printf("Enter your new password :");
  	get_inp(password, 24);
  	if(strlen(password) > 7) {
    	printf("Enter the size of address :");
    	scanf("%d", &size);
    	if (size < 1 || 0x3ff < size) {
      		puts("Invalid Size");
      		exit(0);
    	}
    	ptr->addr_size = size;
    	ptr->addr = malloc(size + 1);
    	printf("Enter your address :");
    	get_inp(ptr->addr, size);

    	op = 0;
    	puts("Would you like to deposit money now ?");
    	printf("1. Yes\n2. No\nEnter choice :");
    	scanf("%d",&op);
    	
    	amount = 0;
    	if (op == 1) {
    		printf("Enter the amount :");
      		scanf("%d", &amount);
    	}

    	ptr->money = amount;
    	g_data[idx] = ptr;
    	h_obj = malloc(0x10);
    	h_obj->phash = hasher(password, 0x984780);
    	h_obj-uhash = hasher(ptr, 0x12d1aa);
    	g_table[idx] = h_obj;
    	puts("Registeration Successful");
  	}

  	puts("Minimum 8 characters");
  	exit(0);
}


void login()
{
  	char username[32];
  	char password[24];
  
  	printf("Enter your username :");
  	get_inp(username, 20);
  	idx = -1;
  	i = 0;
  	while (i < 10) {
    	if (g_table[i]) {
      		if (hasher(username, 0x12d1aa) == g_table[i]->uhash) {
        		puts("Username found");
        		idx = i;
        		break;
      		}
    	}
    	i = i + 1;
  	}
  	
  	if (i == 10) {
    	puts("User does not exist");
    	exit(0);
  	}
  	
  	printf("Enter your password :");
  	get_inp(password, 24);
  	
  	if (hasher(password,0x984780) != g_table[idx]->phash) {
    	puts("Incorrect username of password");
    	exit(0);
  	}
  	
  	puts("Login Successful");
  	amount = 0;
  	size = 0;
  	print_menu();
  	op = 0;
  	scanf("%d", &op);
  	switch(op) {
  		
  		default:
    		puts("Logging out");
    		return;

  		case 1:
    		printf("Enter deposit amount :");
    		scanf("%lu", &amount);
    		g_data[idx]->money += amount;
    		printf("Your current balance = %lu\n", g_data[idx]->money);
    		break;
  	
  		case 2:
    		printf("Enter withdraw amount :");
    		scanf("%lu", &amount);
    		g_data[idx]->money -= amount;
    		printf("Your current balance = %lu\n", g_data[idx]->money);
    		break;
  		
  		case 3:
    		printf("Enter your new username :");
    		memset(username, -1, 24);
    		get_inp(username, 20);
    		i = 0;
    		while (i < 10) {
      			if (g_data[i])
        			if(!strncmp(username, g_data[i]->username, 20)) {
          				puts("Username taken");
          				exit(0);
        			}
      			
      			i = i + 1;
    		}
    		memset(g_data[i]->username, 0, 24);
    		strncpy(g_data[i]->username, username, 24);
    		g_table[idx]->uhash = hasher(g_data[i]->username, 0x12d1aa);
    		puts("Username successfully updated");
    		break;

  		case 4:
    		printf("Enter your new password :");
    		get_inp(password, 24);
    		if(strlen(password) < 8) {
      			puts("Minimum 8 characters");
      			exit(0);
    		}
    		
    		g_table[idx]->uhash = hasher(password, 0x984780);
    		puts("Password successfully reset");
    		break;
  	
  		case 5:
    		printf("Enter the size of new addresss :");
    		scanf("%d", &size);
    		if(g_data[idx]->addr_size < size) {
      			puts("Invalid Size; size too large");
      			return;
    		}
    		
    		edit_addr(g_data[idx]->addr, size);
    		puts("Address successfully updated");
  		}
}


long hasher(char *pcParm1,long lParm2)
{ 
  cVar1 = *pcParm1;
  local_28 = lParm2;
  local_20 = pcParm1;
  while (local_c = (int)cVar1, *local_20 != 0) {
    local_28 = (long)local_c + local_28 * 0x41;
    cVar1 = local_20[1];
    local_20 = local_20 + 1;
  }
  return local_28;
}


void print_menu()
{
  puts("What servie would you like");
  puts("\t1. Deposit money");
  puts("\t2. Withdraw money");
  puts("\t3. Change username");
  puts("\t4. Reset password");
  puts("\t5. Update address");
  puts("\t6. Logout");
  printf("Enter your choice :");
}


void edit_addr(undefined8 uParm1,uint uParm2)
{
  printf("Enter the new address :");
  get_inp(uParm1, uParm2);
}

