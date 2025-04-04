import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def dfs(x,color):
    global endTrigger
    
    visited[x] = color
    
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i,-color)
        elif visited[i] == color:
            endTrigger = True
            return
    

T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    endTrigger = False
    
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1,n+1):
        if visited[i] == 0:
            dfs(i,1)
    if endTrigger:
        print("impossible")
    else:
        print("possible")