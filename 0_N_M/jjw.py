N, M = map(int, input().split())
arr = []
visited = [0] * (N + 1)


def dfs(depth):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = i
            arr.append(i)
            dfs(depth + 1)
            arr.pop()
            visited[i] = 0


dfs(0)
