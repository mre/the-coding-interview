#include <iostream>

//Function to calculate number of integers in a given number.
int integer_length(long long int n){
    int length = 0;
    while (n!=0){
        length++;
        n=n/10;
    }
    return length;
}

//Driver function.
int main(){
    std::cout << integer_length(34) << std::endl;
    std::cout << integer_length(6) << std::endl;
    std::cout << integer_length(785416931) << std::endl;
}