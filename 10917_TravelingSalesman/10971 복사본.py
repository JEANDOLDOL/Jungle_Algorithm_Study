import sys
input = sys.stdin.readline

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]


visited = [False] * n
minval = 0

def travel(cnt, start, now, cost):
    global minval
    
    for i in range(n):
        if not visited[i] and city[now][i]:
            visited[i] = True
            travel(cnt+1, start, i, cost+city[now][i])
            visited[i] = False
    
    if cnt == n and city[now][start]:
        cost += city[now][start]
        
        if cost < minval or minval == 0:
            minval = cost
            return
    
    # for i in range(n):
    #     if not visited[i] and city[now][i]:
    #         visited[i] = True
    #         travel(cnt+1, start, i, cost+city[now][i])
    #         visited[i] = False


for i in range(n):
    visited[i] = True
    travel(1,i,i,0)
    visited[i] = False
    
print(minval)