#include <stdio.h>
static int sum;
static int minsum = 2147483647;

void travel(int depth, int start, int max, int visited[max], int arr[max][max])
{
    /*
    종료 조건
    */
    if (depth == max - 1)
    {
        if (arr[start][0] != 0)
        {
            sum += arr[start][0];
            if (minsum > sum)
            {
                minsum = sum;
            }
            sum -= arr[start][0];
        }
        return;
    }
    // 시작 도시는 정해줬으니 두번째 도시부터 탐색
    for (int i = 1; i < max; i++)
    {
        if ((visited[i] == 0) && (arr[start][i] != 0))
        {
            visited[i] = 1;
            sum += arr[start][i];
            // depth += 1; 말고, 재귀로 부를때 더해야 올바른 답이 나옴, 왜지
            travel(depth + 1, i, max, visited, arr);
            visited[i] = 0;
            sum -= arr[start][i];
        }
    }
}

int main()
{
    int N = 0;
    scanf("%d", &N);
    int visited[N];
    for (int i = 0; i < N; i++)
    {
        visited[i] = 0;
    }

    int arr[N][N];
    for (int i = 0; i < N; i++)
    {
        for (int e = 0; e < N; e++)
        {
            scanf("%d", &arr[i][e]);
        }
    } // why is this working?

    travel(0, 0, N, visited, arr);

    printf("%d", minsum);
    return 0;
}

///
