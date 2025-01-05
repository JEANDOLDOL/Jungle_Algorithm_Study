import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int,input().split())

graph = [[0 for _ in range(N)] for _ in range(M)]

cor = []
for _ in range(K):
  cor.append(list(map(int,input().split())))

for i in cor:
  for e in range(i[0], i[2]):
    for d in range(i[1],i[3]):
      graph[M - 1 - d][e] = 1
for i in graph:
  print(i)  
  
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0

def dfs(x,y):
  global count
  if x<0 or x >= M or y<0 or y>=N:
    return 0
  if graph[x][y] == 1:
    return 0
  graph[x][y] = 1
  count += 1
  
  for i in range(4):
    dfs(x+dx[i],y+dy[i])
    
  return count

result = []
for i in range(M):
  for e in range(N):
    cnt = dfs(i,e)
    if cnt:
      result.append(cnt)
      count = 0
      
result.sort()
print(len(result))
for i in result:
    print(i, end=' ')
  