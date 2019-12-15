#include <stdio.h>

int main(__attribute__ ((unused)) const int argc, const char* argv[]) {
    for (int i = 0; argv[1][i] != '\0'; i++) {
        printf("%c", argv[1][i] == '\n' ? '\n' : 'z' - (argv[1][i] - 'a'));
    }
}
