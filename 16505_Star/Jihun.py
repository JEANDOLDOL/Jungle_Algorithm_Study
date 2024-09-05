def Rec(i, x, y, count, arr):
    if i == 0:
        arr[x][y] = True
    
    else:
        count //= 2
        Rec(i-1, x, y, count, arr)
        Rec(i-1, x+count, y, count, arr)
        Rec(i-1, x, y+count, count, arr)


N = int(input())

count = 2**N

arr = [[False for _ in range(count)] for _ in range(count)] 

Rec(N, 0, 0, count, arr)

for i in range(count):
    for j in range(count - i):
        if arr[i][j]:
            print("*", end="")
        else:
            print (" ", end="")
    print("")