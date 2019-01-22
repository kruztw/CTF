#include <stdio.h>
#include <string.h>

int main()
{
    FILE *file;

    char password[8];  //$rbp-0x10
    char buffer[8];    //$rbp-0x20
    fgets(buffer, sizeof(buffer), stdin);
    strcat(buffer, "bbbbbbbbbb"); 

    file = fopen("password.txt", "r");
    fgets(password, sizeof(password), file);

    puts(buffer);

    return 0;
}