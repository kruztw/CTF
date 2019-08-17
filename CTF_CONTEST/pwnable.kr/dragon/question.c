/* arranged in memory order */
struct dragon
{
	void (*print_info)(struct dragon*); //+0x0
	int   type;        //+0x4
	char  HP;          //+0x8
	short regeneration;//+0x9
	int   damage;      //+0xc
}

struct player
{
	int type; //+0x0
	int HP;   //+0x4
	int MP;   //+0x8
	void (*print_info)(struct player*); //+0xc
}

int count;
int main()
{
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  puts("Welcome to Dragon Hunter!");
  PlayGame();
  return 0;
}


void PlayGame()
{
  int op;
  
  while( true ) {
    while( true ) {
      puts("Choose Your Hero\n[ 1 ] Priest\n[ 2 ] Knight");
      op = GetChoice();
      if ((op != 1) && (op != 2)) break;
      FightDragon(op);
    }
    if (op != 3) break;
    SecretLevel();
  }
  return;
}


void SecretLevel(void)
{
  int iVar1;
  int in_GS_OFFSET;
  char pw [10];
  int local_10;
  
  printf("Welcome to Secret Level!\nInput Password : ");
  scanf("%10s", pw);
  
  if(strcmp(pw,"Nice_Try_But_The_Dragons_Won\'t_Let_You!")) {
      puts("Wrong!\n");
      exit(-1);
  }

  system("/bin/sh");
  return;
}



int GetChoice()
{
  int choice[3];
  
  do{
  	scanf("%d", choice);
  }while(getchar() != '\n')

  return choice[0];
}


void PrintPlayerInfo(struct *_player_ptr)
{
  if (_player_ptr->type == 1)
      printf("[ Priest ] %d HP / %d MP\n\t[ 1 ] Holy Bolt ...", _player_ptr->HP, _player_ptr->MP);
  else if (_player_ptr->type == 2)
      printf("[ Knight ] %d HP / 0 Mana\n\t[ 1 ] Crash\n\t...", _player_ptr->HP);
}

void PrintMonsterInfo(struct dragon* _player_ptr)
{
  if (_player_ptr->type == 0)
    printf("[ Baby Dragon ] %d HP / 30 Damage / +5 Life R...", _dragon_ptr->HP);
  else 
    printf("[ Mama Dragon ] %d HP / 10 Damage / +4 Life R...", _dragon_ptr->HP);
}


void FightDragon(int _op)
{
  struct *player_ptr;
  struct dragon *dragon_ptr;
  void *name;
  int result;
  
  player_ptr = (struct player*)malloc(0x10);
  dragon_ptr = (struct dragon *)malloc(0x10);
  if (Count % 2 == 0) {
    Count = Count + 1;
    dragon_ptr->type = 0;
    dragon_ptr->hp = 50;
    dragon_ptr->regeneration = 5;
    dragon_ptr->damage = 30;
    dragon_ptr->print_info = PrintMonsterInfo;
    puts("Baby Dragon Has Appeared!");
  }
  else {
    Count = Count + 1;
    dragon_ptr->type = 1;
    dragon_ptr->hp = 80;
    dragon_ptr->regeneration = 4;
    dragon_ptr->damage = 10;
    dragon_ptr->print_info = PrintMonsterInfo;
    puts("Mama Dragon Has Appeared!");
  }
  if (_op == 1) {
    *player_ptr     = 1;
    player_ptr->HP  = 42;
    player_ptr->MP  = 50;
    player_ptr->print_info = PrintPlayerInfo;
    result = PriestAttack(player_ptr,dragon_ptr);
  }
  else if(op == 2){
    player_ptr->type = 2;
    player_ptr->HP   = 50;
    player_ptr->MP   = 0;
    player_ptr->print_info = PrintPlayerInfo;
    result = KnightAttack(player_ptr,dragon_ptr);
  }
  else return;

  if (result == 0)
    puts("\nYou Have Been Defeated!");
  else {
    puts("Well Done Hero! You Killed The Dragon!");
    puts("The World Will Remember You As:");
    name = malloc(0x10); // uaf 
    scanf("%16s", name); // control eip
    puts("And The Dragon You Have Defeated Was Called:");
    dragon_ptr->print_info; // get shell
  }

  free(player_ptr);
  return;
}




int PriestAttack(struct *_player_ptr, struct dragon *_dragon_ptr)
{
  int op;
  
  while( true ) {
  	_player_ptr->print_info(_player_ptr);
  	_dragon_ptr->print_info(_dragon_ptr);

    op = GetChoice();
    if(op == 1){
		if(_player_ptr->MP < 10) 
            puts("Not Enough MP!");
        else {
            printf("Holy Bolt Deals %d Damage To The Dragon!\n", 20);
            _dragon_ptr->HP -= 20;
            _player_ptr->MP -= 10;
            printf("But The Dragon Deals %d Damage To You!\n", _dragon_ptr->damage);
            _player_ptr->HP -= _dragon_ptr->damage;
            printf("And The Dragon Heals %d HP!\n", _dragon_ptr->regeneration);
            _dragon_ptr->HP += _dragon_ptr->regeneration;
        }
    }
    else if (op == 2) {
      	puts("Clarity! Your Mana Has Been Refreshed");
      	_player_ptr->MP = 50;
      	printf("But The Dragon Deals %d Damage To You!\n", _dragon_ptr->damage);
      	_player_ptr->HP -= _dragon_ptr->damage;
      	printf("And The Dragon Heals %d HP!\n", _dragon_ptr->regeneration);
      	_dragon_ptr->HP += _dragon_ptr->regeneration;
    }
    else if(op == 3){
        if(_player_ptr->MP < 35) 
          	puts("Not Enough MP!");
        else{
          	puts("HolyShield! You Are Temporarily Invincible...");
          	printf("But The Dragon Heals %d HP!\n", _dragon_ptr->regeneration);
          	_dragon_ptr->HP += _dragon_ptr->regeneration;
          	_player_ptr->MP -= 35;
        }
    }
    
    /* uaf bug */
    if(_player_ptr->HP < 1) break;
    if(_dragon_ptr->HP < 1) {
        free(_dragon_ptr);  
        return 1;
    }
  }

  free(_dragon_ptr);
  return 0;
}


int KnightAttack(struct *_player_ptr, struct *_dragon_ptr)
{
  int op;
  
  while( true ) {
    _player_ptr->print_info;
    _dragon_ptr->print_info;

    op = GetChoice();
    if (op == 1) {
      	printf("Crash Deals %d Damage To The Dragon!\n", 20);
	  	_dragon_ptr->HP -= 20;
      	printf("But The Dragon Deals %d Damage To You!\n", _dragon_ptr->damage);
      	_player_ptr->HP -= _dragon_ptr->damage;
      	printf("And The Dragon Heals %d HP!\n", _dragon_ptr->regeneration);
      	_dragon_ptr->HP += _dragon_ptr->regeneration;
    }
    else if(op == 2){
        printf("Frenzy Deals %d Damage To The Dragon!\n", 40);
        _dragon_ptr->HP -= 40;
        puts("But You Also Lose 20 HP...");
        _player_ptr->HP -= 20;
        printf("And The Dragon Deals %d Damage To You!\n", _dragon_ptr->damage);
        _player_ptr->HP -= _dragon_ptr->damage;
        printf("Plus The Dragon Heals %d HP!\n", _dragon_ptr->regeneration);
        _dragon_ptr->HP += _dragon_ptr->regeneration;
    }

    if (_player_ptr->HP < 1) break;
    if (_dragon_ptr->HP < 1) {
      	free(_dragon_ptr);
      	return 1;
    }
  }

  free(_dragon_ptr);
  return 0;
}

