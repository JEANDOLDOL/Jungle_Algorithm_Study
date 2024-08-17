#include <stdio.h>
#include <stdlib.h>

int compare(int *A, int *B){

}

int main() {
    int n;
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) {
        return 1;
    }

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    //여기에 정렬을 하는 뭔가가 들어가야하는데...
    qsort(arr, n, sizeof(int), compare);


    for (int i = 0; i < n; i++) {
        printf("%d\n", arr[i]);
    }
    
    free(arr);
    
    return 0;
}