#include<stdio.h>
int sum(int arr[], int n) 
{ 
    int sum = 0; 
    for (int i = 0; i < n; i++) 
    sum += arr[i]; 
  
    return sum+n; 
} 
  
int main() 
{ 
    int arr[] = {1,2,3,4}; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    printf("%d",sum(arr, n)); 
    return 0; 
} 