import sys

input = sys.stdin.readline

N = int(input())
day = []
money = []

dp = [0] * (N + 1)
max_value = 0

for _ in range(N):
    x, y = map(int, input().split())
    day.append(x)
    money.append(y)

for i in range(N-1, -1, -1):
    if i + day[i] <= N: # 상담을 할 수 있다면
        dp[i] = max(dp[i+1], money[i] + dp[i + day[i]]) # 다음날부터 계산된 최대 이익 or 현재 상담의 수익 + 그 상담이 끝난 날부터 최대 이익.
    else: # 상담을 할 수 없는 경우 / i + day[i] > N
        dp[i] = dp[i+1]

print(dp[0])

# i = 6일때:
# i + T[6] = 6 + 2 = 8 > 7 상담 불가
# 따라서 dp[6] = dp[7] = 0.
#
# i = 5일때:
# i + T[5] = 5 + 4 = 9 > 7 상담 불가
# 따라서 dp[5] = dp[6] = 0.
#
# i = 4일때:
# i + T[4] = 4 + 2 = 6, 상담 가능
# dp[4] = max(dp[5], P[4] + dp[6]) = max(0, 15 + 0) = 15.
#
# i = 3일때:
# i + T[3] = 3 + 1 = 4, 상담 가능
# dp[3] = max(dp[4], P[3] + dp[4]) = max(15, 20 + 15) = 35.
#
# i = 2일때:
# i + T[2] = 2 + 1 = 3, 상담 가능
# dp[2] = max(dp[3], P[2] + dp[3]) = max(35, 10 + 35) = 45.
#
# i = 1일때:
# i + T[1] = 1 + 5 = 6, 상담 가능
# dp[1] = max(dp[2], P[1] + dp[6]) = max(45, 20 + 0) = 45.
#
# i = 0일때:
# i + T[0] = 0 + 3 = 3, 상담 가능
# dp[0] = max(dp[1], P[0] + dp[3]) = max(45, 10 + 35) = 45.
