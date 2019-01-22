#include <stdio.h>
#include <string.h>

int main()
{
    FILE *file;

    char password[20];  //$rbp-0x20
    char buffer[8];    //$rbp-0x30
    fgets(buffer, sizeof(buffer), stdin);
    strcat(buffer, "bbbbbbbbbb"); 

    file = fopen("password.txt", "r");
    fgets(password, sizeof(password), file);

    puts(buffer);

    return 0;
}

echo "password" > password.txt
gcc bug.c -o bug -fno-stack-protector
./bug
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

