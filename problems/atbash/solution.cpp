#include <iostream>
#include <string>

int main(int, const char* argv[]) {
    std::string s = argv[1];
    for (auto c: s) {
        std::cout << (c == '\n' ? c : (char) ('z' - (c - 'a')));
    }
}
