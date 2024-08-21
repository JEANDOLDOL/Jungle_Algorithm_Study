import collections
import sys
input = sys.stdin.readline

# Input
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]


# 
distance = [[0] *m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# Init Queue 
queue = collections.deque()


def bfs(Dx,Dy):
    while queue:
        x,y = queue.popleft()
        if graph[Dx][Dy] == 'S':
            return distance[Dx][Dy]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # ny nx가 맵 안에 있다면 
            if 0 <= nx < n and 0 <= ny < m:
                # 현재가 고슴도치이고 ny nx 가 움직일수 있는 곳이라면
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S' 
                    # 그 위치에 +1 
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append ((nx,ny))
                # 현재가 물이고 ny nx 가 움직일수 있는 곳
                elif (graph[nx][ny] =='.' or graph[nx][ny] =='S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    queue.append((nx,ny))
    return "KAKTUS"

# 고슴도치와 비버집 위치 넣어주기
for x in range(n):
    for y in range(m):
        if graph[x][y] == 'S':
            queue.append((x,y))
        elif graph[x][y] == 'D':
            Dx,Dy = x,y

# 물 시작점 넣어주기
for x in range(n):
    for y in range(m):
        if graph[x][y] == '*':
            queue.append((x,y))

print(bfs(Dx,Dy))