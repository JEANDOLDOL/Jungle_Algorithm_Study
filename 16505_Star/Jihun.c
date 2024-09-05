#include <stdio.h>
#include <stdlib.h>

void Rec(int N, int x, int y, int count, char** arr)
{
    if(N == 0)
        arr[x][y] = '*';
    
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

    char** arr = (char**)malloc(sizeof(char*)*count);
    for(int i = 0; i < count; i++)
    {
        arr[i] = (char*)malloc(sizeof(char)*count);
        for(int j = 0; j < count; j++)
        {
            arr[i][j] = ' ';
        }
    }

    Rec(N, 0, 0, count, arr);

    for(int i = 0; i < count; i++)
    {
        for(int j = 0; j < count-i; j++)
        {
            printf("%c", arr[i][j]);
        }
        printf("\n");
    }

    for(int i = 0; i < count; i++)
    {
        free(arr[i]);
    }
    free(arr);

    return 0;
}