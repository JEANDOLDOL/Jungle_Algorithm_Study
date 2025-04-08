import heapq
import sys

input = sys.stdin.readline

def wes():
    global result
    
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(heap,i)
        
    while heap:
        temp = heapq.heappop(heap)
        result.append(temp)
        for e in question[temp]:
            indegree[e] -= 1
            if indegree[e] == 0:
                heapq.heappush(heap,e)

N, M = map(int, input().split())

question = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
result = []
heap = []

for _ in range(M):
    a, b = map(int,input().split())
    question[a].append(b)
    indegree[b] += 1
    
wes()
    
print(" ".join(map(str, result)))