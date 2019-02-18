#include <iostream>

//Function to find the number of closed loops in a given number.
int closed_loops(int n){
    int counter = 0;
    while(n!=0){
        int r = n%10;
        if ((r==6) || (r==9) || (r==0))
            counter++;
        if (r==8)
            counter+=2;
        n=n/10;
    }
    return counter;
}

// Driver function.
int main() {
    int num1 = 2876;
    int num2 = 7589;
    int num3 = 1075;
    std::cout << closed_loops(num1) << std::endl;
    std::cout << closed_loops(num2) << std::endl;
    std::cout << closed_loops(num3) << std::endl;
}