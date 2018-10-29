#include <stdio.h>

int main() {
    char string[100] = "Hello hello asdsa";  //Enter your string here


    int i, letters, longest = 0, longest_pos = 0;

    for (i = 0; string[i] != '\0'; i++) {
        for (letters = 0; string[i] != '\0' && string[i] != ' '; i++) {
            letters++;  
        }
        if (letters > longest) {
            longest = letters;
            longest_pos = i - longest;
        }
    }    
    printf("longest word: %d letters, '%.*s'\n",
           longest, longest, string + longest_pos);

    return 0;
}