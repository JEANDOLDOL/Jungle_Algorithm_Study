#include <stdio.h>


void Sort(int *arr, int n)
{
    int min = 0;
    int temp = 0;
    for (int i = 0; i < n; i++)
    {
        min = i;
        for (int j = i; j < n; j++)
        {
            if (arr[min] > arr[j])
            {
                min = j;
            }
        }
        temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }
}

int main()
{
    int n = 0;
    scanf("%d", &n);

    int arr[n];

    for(int i =0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    Sort(arr,n);

    for(int i =0; i < n; i++)
    {
        printf("%d\n", arr[i]);
    }
}