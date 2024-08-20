#include <stdio.h>

void DFS(int M, int N, int x, int y, char arr[M][N])
{
    arr[x][y] = 2;
    int dx[4] = {0,0,1,-1};
    int dy[4] = {1,-1,0,0};

    for(int i = 0; i < 4; i++)
    {
        int curX = x + dx[i];
        int curY = y + dy[i];
        if(curX < 0 || curX >= M || curY < 0 || curY >= N)
            continue;
        
        if(arr[curX][curY] == 1)
            DFS(M,N,curX, curY, arr);
    }
}

int main()
{
    int re = 0;
    scanf("%d", &re);
    for(int r = 0; r < re; r++)
    {
        int M,N,K,a,b;
        scanf("%d %d %d", &M, &N, &K);

        char arr[M][N];
        for(int i = 0; i < M; i++)
        {
            for(int j = 0; j < N; j++)
            {
                arr[i][j] = 0;
            }
        }
        for(int i = 0; i < K; i++)
        {
            scanf("%d %d", &a, &b);
            arr[a][b] = 1;
        }
        //입력 완료

        int count = 0;
        for(int i = 0; i < M; i++)
        {
            for(int j = 0; j < N; j++)
            {
                if(arr[i][j] == 1)
                {
                    DFS(M,N,i,j,arr);
                    count++;
                }
            }
        }
        printf("%d\n", count);
    }
    

    return 0;
}