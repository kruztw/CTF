#include <stdio.h>

int main()
{
    unsigned int list[6];
    unsigned int answer;

    for(int i = 0; i<=4; i++)
        list[i] = i*i + 9029;

    int v1, v2, v3, v4;

    for(int i = 5; i<= 0x19965; i++){
        v1 = list[(i+4)%5];
        v2 = v1 - list[(i+3)%5];
        v3 = list[(i+2)%5];
        v4 = v3 - list[(i+1)%5] + v2;
        answer = v4 + 4660*list[i%5];
        list[i%5] = answer;
    }

    printf("answer = %u\n", answer);

    return 0;
}
