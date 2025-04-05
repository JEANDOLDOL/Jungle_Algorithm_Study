from collections import deque
import sys

input = sys.stdin.readline

def wesang():
    queue = deque()
    result = []
    
    for i in range(1,N + 1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        target = queue.popleft()
        result.append(target)
        
        for e in graph[target]:
            indegree[e] -= 1
            if indegree[e] == 0:
                queue.append(e)
                
    for j in result:
        print(j, end=" ")

N,M = map(int,input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
wesang()