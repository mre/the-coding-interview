#include <stdio.h>
#include <stdlib.h>

#define MAX_LEN 100

int main()
{
    int x, y;
    int loops = 0;
    char s[MAX_LEN];
    char *p;
    printf("Enter number to count loops: ");
    scanf("%d", &x);
    y = x;

    sprintf(s, "%d", x);
    p = s;
    while (*p != '\0')
    {
        if (*p == '6')
            loops++;
        else if (*p == '8')
            loops += 2;
        else if (*p == '9')
            loops++;
        else if (*p == '0')
            loops++;
        p++;
    }
    printf("%d has %d loops\n", y, loops);
    return 0;
}
