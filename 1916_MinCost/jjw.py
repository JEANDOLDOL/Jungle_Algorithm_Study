import sys


INF = sys.maxsize


def djik(n):
    temp = 0
    # 이 부분 최소값 뽑으려 했던 거니까 heapQ사용하면 될듯.
    # for i in


# 도시의 개수
N = int(input())
# 버스의 개수
M = int(input())

# 이런식으로 해보고 안되면 선형 그래프를 사용하자.
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    s, d, c = map(int, input().split())
    graph[s][d] = c

for i in range(N + 1):
    graph[i][i] = 0
    graph[0][i] = 0
    graph[i][0] = 0

print(graph)
