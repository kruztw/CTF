#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int main() {
    char *plaintext = NULL;
    char *one_time_pad = NULL;
    char *ciphertext = NULL;
    size_t flag_length = 0;
    FILE *flag = fopen("flag.txt", "r");
    FILE *urandom = fopen("/dev/urandom", "r");
    assert(flag && urandom);

    /*
     * Get flag length, and allocate memory for the plaintext,
     * one-time pad and ciphertext.
     */
    fseek(flag, 0, SEEK_END);
    flag_length = ftell(flag);
    rewind(flag);

    plaintext = malloc(flag_length + 1);
    one_time_pad = malloc(flag_length + 1);
    ciphertext = malloc(flag_length + 1);
    assert(plaintext && one_time_pad && ciphertext);

    /* Read the plaintext and the one-time-pad */
    fread(plaintext, flag_length, 1, flag);
    fread(one_time_pad, flag_length, 1, urandom);
    plaintext[flag_length] = '\0';
    one_time_pad[flag_length] = '\0';

    /* Make sure that the one-time-pad isn't too short. */
    assert(strlen(plaintext) == strlen(one_time_pad));

    for (int i = 0; i < flag_length; i++) {
        ciphertext[i] = plaintext[i] ^ one_time_pad[i];
    }

    fwrite(ciphertext, flag_length, 1, stdout);
    return 0;
}