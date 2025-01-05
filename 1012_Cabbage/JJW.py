from collections import deque

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, e):
    q = deque()
    q.append((i, e))
    graph[e][i] = 0  # 배추 할당

    while q:
        x, y = q.popleft()
        for k in range(4):
            new_x = x + dx[k]
            new_y = y + dy[k]
            if 0 <= new_x < M and 0 <= new_y < N and graph[new_y][new_x] == 1:
                q.append((new_x, new_y))
                graph[new_y][new_x] = 0  # 인접 배추 할당
    return


for _ in range(T):
    count = 0
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for e in range(N):
        for i in range(M):
            # 순서 주의
            if graph[e][i] == 1:
                bfs(i, e)
                count += 1

    print(count)    
