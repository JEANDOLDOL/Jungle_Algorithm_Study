import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    farm[a][b] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if farm[nx][ny] == 1:
                queue.append((nx, ny))
                farm[nx][ny] = 0

for _ in range(n):
    M, N, K = map(int,input().split())
    farm = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int,input().split())
        farm[x][y] = 1

    bug = 0
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1:
                bfs(i, j)
                bug += 1
    print(bug)

