#include <iostream>

int sum_of_multiples(int n){
    int sum = 0;
    for(int i=3;i<n;i++){
        if((i%3==0) || (i%5==0))
            sum+=i;
    }
    return sum;
}

int main(){
    std::cout << sum_of_multiples(1000);
}
