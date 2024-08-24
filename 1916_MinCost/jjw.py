import sys

INF = sys.maxsize

def djik(n):
    temp = 0
    for i in    


# 도시의 개수
N = int(input())
# 버스의 개수
M = int(input())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    s, d, c = map(int, input().split())
    graph[s][d] = c

for i in range(N + 1):
    graph[i][i] = 0
    graph[0][i] = 0
    graph[i][0] = 0

print(graph)
