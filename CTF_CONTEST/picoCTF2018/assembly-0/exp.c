#include <stdio.h>

extern int asm0(int a, int b);

int main()
{
    printf("%d\n", asm0(0xd8, 0x7a));
    return 0;
}
