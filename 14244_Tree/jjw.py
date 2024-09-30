n, m = map(int, input().split())

if m == 2:
    for i in range(n - 1):
        print(i, i + 1)

else:
    print("0 1")
    for i in range(2, m + 1):
        print(1, i)
    for j in range(m, n - 1):
        print(j, j + 1)
