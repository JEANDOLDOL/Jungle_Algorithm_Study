def Rec(N, x, y):
    if N == 1:  # 가장 작은단위
        arr[x][y] = True
        return

    triple = N//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: 
                continue
            Rec(triple, x+(triple*i), y+(triple*j))
    

N = int(input())

arr = [[False for _ in range(N)] for _ in range(N)]

Rec(N, 0,0)


for i in range(N):
    for j in range(N):
        if arr[i][j]:
            print("*", end="")
        else:
            print(" ", end="")
    print()