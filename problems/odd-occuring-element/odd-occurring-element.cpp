#include <iostream>

int odd_occuring_element(int *a,int n){
    int x = 0;
    for(int i=0;i<n;i++){
        x = x^a[i];
    }
    return x;
}

int main() {
    int array_1[]={1,1,2,2,3,4,4};
    int array_2[]={1,1,4,4,10,10,24,2,2,3,3};
    int n1 = sizeof(array_1)/sizeof(array_1[0]);
    int n2 = sizeof(array_2)/sizeof(array_2[0]);
    std::cout << odd_occuring_element(array_1,n1) << std::endl;
    std::cout << odd_occuring_element(array_2,n2) << std::endl;
}
