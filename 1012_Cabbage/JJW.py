import sys
sys.setrecursionlimit(10000)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def FindCabage(graph, x, y, width, height):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < width)and(0 <= ny < height):
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                FindCabage(graph, nx, ny, width, height)
        

t = int(input()) 

for i in range(t):
    m,n,k = map(int,input().split())
    
    farm = [[0] * m for _ in range(n)]
    worm = 0
    
    for e in range(k):
        a,b = map(int,input().split())
        farm[b][a] = 1
        
    for i in range(n):
        for e in range(m):
            if farm[i][e] == 1:
                FindCabage(farm,e,i,m,n)
                worm += 1
    
    print(worm)