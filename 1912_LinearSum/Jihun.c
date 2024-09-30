#include <stdio.h>


int main()
{
    int N = 0;
    scanf("%d", &N);

    int arr[N];
    for(int i = 0; i < N; i++)
    {
        scanf("%d", &arr[i]);
    }
    
    int max = arr[0], sum = 0;
    for(int i = 0; i < N; i++)
    {
        sum += arr[i];
        if(sum > max)
            max = sum;
        if(sum < 0)
            sum = 0;
    }

    printf("%d", max);

    return 0;
}