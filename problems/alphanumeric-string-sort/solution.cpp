#include <iostream>
#include <string>
#include <algorithm>

int main(int, char* argv[]) {
    std::string input = argv[1];
    std::sort(input.begin(), input.end());

    std::string lower, upper, even, odd;
    for (auto c: input) {
        if ('a' <= c && c <= 'z') {
            lower += c;
        } else if ('A' <= c && c <= 'Z') {
            upper += c;
        } else if (int(c) % 2 == 0) {
            even += c;
        } else {
            odd += c;
        }
    }

    std::cout << lower << upper << even << odd << std::endl;
}
