#include <stdio.h>

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);

    for(int i = 0; i < m; i++)
        printf("0 %d\n", i+1);
    for(int i = m; i < n-1; i++)
        printf("%d %d\n", i, i+1);

    return 0;
}