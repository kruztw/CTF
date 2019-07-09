#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv){

    assert(argc==3);
    int time = atoi(argv[1]);
    int captcha = atoi(argv[2]);

    srand(time);

    int rands[8];
    for(int i = 0;i <= 7; i+=1)
        rands[i] = rand();

    return captcha - rands[1] + rands[2] - rands[3] + rands[4] + rands[5] - rands[6] + rands[7];
}