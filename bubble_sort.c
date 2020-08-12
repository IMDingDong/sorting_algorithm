#include <stdio.h>

int main(void) {
    int array[10] = {4, 5, 2, 7, 9, 1, 8, 3, 6, 10};
    int i, j, temp;

    for(i=0; i<10; i++) {
        for(j=0; j<9-i; j++){
            if(array[j] > array[j+1]){
                temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }

    for(i=0; i<10; i++) {
         printf("%d", array[i]);
    }
    return 0;
}