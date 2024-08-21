# https://www.acmicpc.net/problem/1012
# 풀이 유도
#1.필드를 돌면서 배추를 찾음.
#2. 배추를 찾으면 카운트 1 업 그리고 DFS로 연결된 배추 다 없에기
# 3. 반복


import sys
sys.setrecursionlimit(10000)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y):  
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n): #필드 안일때
            if field[ny][nx] == 1: #배추일때
                field[ny][nx] = 0 #0으로 만들어서 다시 안들어가게
                dfs(nx, ny) # 제귀



T = int(sys.stdin.readline());

for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    for x in range(m):
        for y in range(n):
            if field[y][x] == 1:
                dfs(x, y)
                count += 1
    print(count)

