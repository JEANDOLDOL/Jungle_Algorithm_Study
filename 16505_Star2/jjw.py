N = int(input())


def star(N, x, y):
    if N == 1:
        return

    # punch mid
    for i in range(N // 3, 2 * (N // 3)):
        for e in range(N // 3, 2 * (N // 3)):
            arr[x + i][y + e] = True

    for i in range(3):
        for e in range(3):
            if i == 1 and e == 1:
                continue
            star(N // 3, x + (N // 3) * i, y + (N // 3) * e)


arr = [[False for _ in range(N)] for _ in range(N)]

star(N, 0, 0)

for i in range(N):
    for j in range(N):
        if not arr[i][j]:
            print("*", end="")
        else:
            print(" ", end="")
    print()
