#include <stdio.h>
#include <stdlib.h>

void location_change(int *A , int *B){
    int temp;
    temp = *A;
    *A = *B;
    *B = temp;
}

int main() {
    int arr_size;
    scanf("%d", &arr_size);

    int *arr = (int *)calloc(arr_size, sizeof(int));
    if (arr == NULL) {
        return 1;
    }

    for (int index = 0; index < arr_size; index++){
        scanf("%d", &arr[index]);
    }

   for (int i = 0; i < arr_size - 1; i++) {
        for (int j = 0; j < arr_size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                location_change(&arr[j], &arr[j + 1]);
            }
        }
    }

    for (int i = 0; i < arr_size; i++){
        printf("%d\n", arr[i]);
    }    

    free(arr);

    return 0;
}