#include <iostream>

//Recursive Function to return the nth number in the fibonacci series.
int fibonacci(int n){
    if(n==0)
        return 0;
    else if (n==1)
        return 1;
    else
        return fibonacci(n-1)+fibonacci(n-2);
}

//Driver Function.
int main() {
    std::cout << fibonacci(3) << std::endl;
    std::cout << fibonacci(4) << std::endl;
    std::cout << fibonacci(8) << std::endl;
}