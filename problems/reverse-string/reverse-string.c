#include <stdio.h>

#define MAX_LEN 100

void reverse(char *message);

int main(void) {
    
    char message[MAX_LEN];
    char c, *p = message;

    printf("Enter a message: ");

    while ((c = getchar()) != '\n' && p < message + MAX_LEN)
        *p++ = c;
    *p = '\0';

    reverse(message);
    printf("Reversal is: ");

    printf("%s\n", message);

    return 0;
}    

void reverse(char *message) {

    char *p = message, *q = message, temp;

    while (*q)
        q++;
    q--;

    while (p < q) {
        temp = *p;
        *p = *q;
        *q = temp;
        p++;
        q--;
    }
}
