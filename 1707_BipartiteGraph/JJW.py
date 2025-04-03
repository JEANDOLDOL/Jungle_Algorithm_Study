import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(x, color):
    global error
    visited[x] = color

    for i in graph[x]:
        if visited[i] == 0:
            dfs(i, -color)
        elif visited[i] == color:
            error = True
            return

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    error = False
    
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(1, V + 1):
        if visited[i] == 0:    
            dfs(i, 1)
                
    print("NO" if error else "YES")
