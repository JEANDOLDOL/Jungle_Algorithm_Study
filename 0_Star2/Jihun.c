#include <stdio.h>
#include <stdlib.h>

void Rec(int N, int x, int y, char** arr)
{
    if(N == 1)
    {
        arr[x][y] = '*';
        return;
    }
    
    int triple = N/3;

    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            if(i == 1 && j == 1) continue; 
            Rec(triple, x + (i*triple), y + (j*triple), arr);
        }
    }
}

int main()
{
    int N = 0;
    scanf("%d", &N);

    char** arr = (char**)malloc(sizeof(char*)*N);
    for(int i = 0; i < N; i++)
    {
        arr[i] = (char*)malloc(sizeof(char)*N);
        for(int j = 0; j < N; j++)
        {
            arr[i][j] = ' ';
        }
    }

    Rec(N, 0, 0, arr);

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            printf("%c", arr[i][j]);
        }
        printf("\n");
    }

    for(int i = 0; i < N; i++)
    {
        free(arr[i]);  
    }

    free(arr);

    return 0;
}