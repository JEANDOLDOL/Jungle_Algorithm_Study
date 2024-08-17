import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, color):
    visited[x] = color
    # dfs lets go
    for i in graph[x]:
        # 연결된 것들이 아직 방문되지 않았다면,
        if visited[i] == 0:
            if dfs(i, -color) == True:
                continue
            else:
                return False
        # 방문했는데 다른 색이라면, ok
        elif visited[x] != visited[i]:
            continue
        else:
            return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        a, b = map(int, input().split())
        # 무방향 그래프이기 때문에
        graph[a].append(b)
        graph[b].append(a)
    is_ebun = True
    for e in range(1, V + 1):
        # 일단 0인것들 visited 1로 마크할거임. 0일때만 방문 안 한 걸로.
        if visited[e] == 0:
            is_ebun = dfs(e, 1)
            if is_ebun == False:
                break
    # 모든 호출에서 살아남았다면
    if is_ebun == True:
        print("YES")
    # 한 번이라도 걸렸다면
    else:
        print("NO")
