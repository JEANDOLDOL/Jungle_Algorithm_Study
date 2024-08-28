N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    T, P = map(int, input().split())
    graph[i].append(T)
    graph[i].append(P)

dp = [0 for _ in range(N + 1)]
# 첫째날부터 끝까지 탐색.
for i in range(N):
    # i에 상담을 시작하고 걸린 시간을 더한 날부터 시작, 마지막 날까지.
    # 그 크기가 인덱스 범위를 넘지 않을 때까지.
    # end_day는 사실필요가 없다 포 문에서 비굘ㄹ 하면서 돌아간다
    end_day = i + graph[i][0]
    if end_day <= N + 1:
        # 그 날 이후로 작업 하나씩 비교
        for e in range(end_day, N + 1):
            if dp[e] < dp[i] + graph[i][1]:
                dp[e] = dp[i] + graph[i][1]

print(dp[N])
