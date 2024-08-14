#include <stdio.h>
#define SIZE 32
static int moved = 0;
void move(int N, int x, int y)
{
    if (N > 1)
    {
        move(N - 1, x, 6 - x - y);
    }
    printf("%d %d\n", x, y);
    moved++;
    if (N > 1)
    {
        move(N - 1, 6 - x - y, y);
    }
}

void multiplyByTwo(int number[], int size)
{
    int carry = 0;
    for (int i = 0; i < size; i++)
    {
        int product = number[i] * 2 + carry;
        number[i] = product % 10;
        carry = product / 10;
    }
}

void subtractOne(int number[], int size)
{
    int i = 0;
    while (number[i] == 0)
    {
        number[i] = 9;
        i++;
    }
    number[i] -= 1; // 0이 아니면 뺌
}

void printNumber(int number[], int size)
{
    int start = size - 1;
    while (start > 0 && number[start] == 0)
        start--; // 0이 아닌 곳부터 시작.

    for (int i = start; i >= 0; i--)
        printf("%d", number[i]);
    printf("\n");
}

// 이걸 써보자 배열에 숫자를 하나씩 저장한다.
void sumArr(int L[], int R[], int sum[])
{ // https://haruhiism.tistory.com/11 <- 아이디어 출처
    int loopIndex, supp = 0;
    for (loopIndex = 0; loopIndex < SIZE; loopIndex++)
    {
        sum[loopIndex] = L[loopIndex] + R[loopIndex] + supp;

        if (sum[loopIndex] > 9)
        {
            sum[loopIndex] -= 10;
            supp = 1;
        }
        else
        {
            supp = 0;
        }
    }
}

int main()
{
    int N = 0;
    scanf("%d", &N);

    int moves[SIZE] = {0};
    moves[0] = 1; //
    for (int i = 0; i < N; i++)
    {
        multiplyByTwo(moves, SIZE);
    }

    subtractOne(moves, SIZE);

    printNumber(moves, SIZE);

    if (N <= 20)
    {
        move(N, 1, 3);
    }
    return 0;
}