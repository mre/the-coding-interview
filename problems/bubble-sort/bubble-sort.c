#include <stdio.h>

void bubblesort(int *v, size_t size){

    int i,j,aux;

    for (i=0; i < size-1; i++) {
        for(j=i+1; j < size; j++) {
            if(v[i] > v[j]) {
                aux=v[i];
                v[i]=v[j];
                v[j]=aux;
            }
        }
    }
}
