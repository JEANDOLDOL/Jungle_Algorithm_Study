#include <stdio.h>
#include <string.h>

int Opposite(int a, int b)
{
    if(a == 1)
    {
        if(b == 2)  return 3;
        else return 2;
    }
    if(a == 2)
    {
        if(b == 1)  return 3;
        else return 1;
    }
    if(a == 3)
    {
        if(b == 2)  return 1;
        else return 2;
    }
    
}

void Hanoi(int n, int from, int to)
{
    if(n == 1)
    {
        printf("%d %d\n", from, to);
    }
    else
    {
        Hanoi(n-1, from, Opposite(from, to));
        printf("%d %d\n", from, to);
        Hanoi(n-1, Opposite(from, to), to);
    }
}

#define MAX_DIGITS 102

// 큰 수 덧셈 함수
void addBigNumbers(char* num1, char* num2, char* result) {
    int carry = 0, i;
    int len1 = strlen(num1);
    int len2 = strlen(num2);
    int max_len = len1 > len2 ? len1 : len2;

    for(i = 0; i < max_len || carry; i++) {
        int sum = carry;
        if(i < len1) sum += num1[len1 - i - 1] - '0';
        if(i < len2) sum += num2[len2 - i - 1] - '0';
        
        result[i] = sum % 10 + '0';
        carry = sum / 10;
    }
    result[i] = '\0';

    // 결과 뒤집기
    for(int j = 0; j < i / 2; j++) {
        char temp = result[j];
        result[j] = result[i - j - 1];
        result[i - j - 1] = temp;
    }
}

// HanoiDP 함수 - 문자열 기반 큰 수를 이용한 DP 계산
void HanoiDP(int n, char dp[][MAX_DIGITS]) {
    strcpy(dp[1], "1");

    for(int i = 2; i <= n; i++) {
        char temp[MAX_DIGITS];
        addBigNumbers(dp[i-1], dp[i-1], temp); // dp[i] = dp[i-1] * 2
        addBigNumbers(temp, "1", dp[i]); // dp[i] += 1
    }
}

// 기존 Opposite와 Hanoi 함수는 그대로 사용

int main()
{
    int n;
    scanf("%d", &n);

    char dp[n+1][MAX_DIGITS];
    for(int i = 0; i < n+1; i++) dp[i][0] = '\0';

    // 이동 횟수 DP로 계산
    HanoiDP(n, dp);
    printf("%s\n", dp[n]);

    // 과정 출력
    if(n <= 20)
    {
        Hanoi(n, 1, 3);
    }

    return 0;
}