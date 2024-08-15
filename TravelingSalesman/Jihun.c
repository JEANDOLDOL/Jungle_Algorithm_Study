#include <stdio.h>
#include <stdlib.h>

static int minCost = (~0);

int Calc(int *route, int** arr, int N)
{
    int sum = arr[route[N-1]][route[0]];
    if(sum == 0) return 0;
    for(int i = 0; i <N-1; i++)
    {
        int from = route[i];
        int to = route[i+1];
        int cost = arr[from][to];
        if(cost == 0) return 0;

        sum += cost;
    }

    return sum;
}

void SetRoute(int* route, int** arr, int N, int curIndex)
{
    if(N <= curIndex)
    {
        int cost = Calc(route, arr, N);
        if(cost < minCost && cost != 0) minCost = cost;
        return;
    }
    for(int i = 0; i < N; i++)
    {
        int flag = 0;
        for(int j = 0; j < curIndex; j++)
        {
            if(route[j] == i)
            {
                flag = 1;
                break;
            }
        }
        if(flag) continue;

        route[curIndex] = i;
        SetRoute(route, arr, N, curIndex + 1);
    }
}

int main()
{
    int N = 0;
    scanf("%d", &N);

    int **arr = (int**)malloc(N* sizeof(int*));

    for(int i = 0; i < N; i++)
    {
        arr[i] = calloc(N, sizeof(int));
        for(int j = 0; j < N; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }
    // 입력 종료. 로직 시작


    int route[N];
    SetRoute(route, arr, N, 0);

    printf("%d", minCost);

    for(int i = 0; i < N; i++) {
        free(arr[i]);
    }
    free(arr);
}