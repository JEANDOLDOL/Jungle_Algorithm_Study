import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

building = [[] for _ in range(N + 1)]
time = [0] * (N + 1)
indegree = [0] * (N + 1)
construct = [0] * (N + 1)

for i in range(1, N + 1):
    temp = list(map(int,input().split()))
    time[i] = (temp[0])
    for e in range(1,len(temp)):
        if temp[e] == -1:
            break
        else:
            building[temp[e]].append(i)
            indegree[i] += 1
            
q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        construct[i] = time[i] 

while q:
    tmp = q.popleft()
    for e in building[tmp]:
        indegree[e] -= 1
        construct[e] = max(construct[e], construct[tmp] + time[e])
        if indegree[e] == 0:
            q.append(e)

for i in range(1,len(construct)):
    print(construct[i])    