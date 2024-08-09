#include <stdio.h>
int sort(int *arr, int n)
{
    int new_arr[n];
    int temp = 0;
    for (int i = 0; i < n; i++)
    {
        for (int e = i; e < n; e++)
        {
            if (arr[i] > arr[e])
            {
                temp = arr[i];
                arr[i] = arr[e];
                arr[e] = temp;
            }
        }
        printf("%d\n", arr[i]);
    }

    return 0;
}

int main()
{
    int num = 0;
    scanf("%d", &num);
    int arr[num];
    for (int i = 0; i < num; i++)
    {
        scanf("%d", &arr[i]);
    }
    sort(arr, num);
    return 0;
}