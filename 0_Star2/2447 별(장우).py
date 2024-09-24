import sys
def star_rec(x, y, N):

    if N == 1:
        arr[x][y] = "*"
        return

    triple = N // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            star_rec(x + i * triple, y + j * triple, triple)


input = sys.stdin.readline
N = int(input())


arr = [[" " for _ in range(N)] for _ in range(N)]

star_rec(0,0, N)

for i in arr:
    for j in i:
        print(j, end="")
    print()