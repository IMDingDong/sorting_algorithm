#include <stdio.h>
#define MAX_SIZE 5

void insertion_sort(int list[], int n) {
    int i, j, key;

    for(i=1; i<n; i++) {
        key = list[i];
        for(j=i-1; j>=0 && list[j]>key; j--) {
            list[j+1] = list[j];
        }
        list[j+1] = key;
    }
}

void main() {
    int i;
    int n = MAX_SIZE;
    int list[n] = {5, 3, 4, 1, 2};

    insertion_sort(list, n);

    for(i=0; i<n; i++) {
        printf("%d\n", list[i]);
    }
}