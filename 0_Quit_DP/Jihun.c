#include <stdio.h>

#define MAX(a,b) (((a)<(b)?(b):(a)))

int main()
{
    int N, a, b;
    scanf("%d", &N);

    int costs[N];
    int prizes[N];

    int DP[N+2];

    for(int i = 0; i < N; i++)
    {
        DP[i] = 0;
        scanf("%d %d", &costs[i], &prizes[i]);
    }
    DP[N] = 0;
    DP[N+1] = 0;

    for(int i = 0; i < N; i++)
    {
        int cost = costs[i];
        int prize = prizes[i];
        
        int newCost = DP[i+1]+prize;
        for(int j = i+1+cost; j <= N+1; j++)
        {
            DP[j] = MAX(DP[j], newCost);
        }
    }

    printf("%d\n", DP[N+1]);

    return 0;
}