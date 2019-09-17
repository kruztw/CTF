int main(int argc,char **argv)
{
  char local_74 [100];
  int *local_10;
  
  local_10 = &argc;
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stdin,(char *)0x0,2,0);
  setvbuf(stderr,(char *)0x0,2,0);
  puts("Simulating loss...");
  lose();
  printf("Hey you! GOT milk? ");
  fgets(local_74,100,stdin);
  printf("Your answer: ");
  printf(local_74);
  lose();
  return 0;
}

