N = int(input())
a, b = map(int, input().split())
M = int(input())
arr = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
min = 9999

for _ in range(M):
    o, k = map(int, input().split())
    arr[o].append(k)
    arr[k].append(o)


def chon(v, num):
    global min
    num += 1
    visited[v] = True

    if v == b:
        if num < min:
            min = num

    for i in arr[v]:
        if not visited[i]:
            chon(i, num)


chon(a, 0)

if min == 9999:
    print(-1)
else:
    print(min - 1)
