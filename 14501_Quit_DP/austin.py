import sys

def max_profit(N, schedule):
    # DP 테이블 초기화: dp[i]는 i일부터 얻을 수 있는 최대 수익
    dp = [0] * (N + 1)
    
    # 뒤에서부터 DP 테이블 채우기
    for i in range(N - 1, -1, -1):
        # 퇴사일을 넘기지 않는 경우
        if i + schedule[i][0] <= N:
            # i일에 상담을 하는 경우와 하지 않는 경우 중 최대값 선택
            dp[i] = max(schedule[i][1] + dp[i + schedule[i][0]], dp[i + 1])
        # i일에 상담을 할 수 없는 경우
        else:
            dp[i] = dp[i + 1] # base case
    
    return dp[0]

# 입력 받기
N = int(sys.stdin.readline().rstrip())
schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 결과 출력
print(max_profit(N, schedule))