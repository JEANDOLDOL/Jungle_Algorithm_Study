#include <stdio.h>
#include <stdlib.h>

void Rec(int N, int x, int y, int count, int* arr)
{
    if(N == 0)
        arr[x] |= 1<<y;
    
    else
    {
        count /= 2;
        Rec(N-1, x, y,count, arr);
        Rec(N-1, x+count, y,count, arr);
        Rec(N-1, x, y+count,count, arr);
    }
}

int main()
{
    int N = 0;
    scanf("%d", &N);
    N++;

    int count = 1;

    for(int i = 0; i < N-1; i++)
    {
        count *= 2;
    }

    int* arr = (int*)calloc(sizeof(int), count);

    Rec(N, 0, 0, count, arr);

    for(int i = 0; i < count-1; i++)
    {
        for(int j = 0; j < count-i; j++)
        {
            printf("%c", (arr[i] & 1<<j ? '*' : ' '));
        }
        printf("\n");
    }
    printf("*");

    free(arr);

    return 0;
}