import sys

# 재귀의 길를 넓히고자, 기약없는 약속을 멀리 두었노라
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    n1, n2, dist = map(int, input().split())
    graph[n1].append([n2, dist])
    graph[n2].append([n1, dist])
# 입력 끝

visited = [-1] * (n + 1)


# 깊이따라 길을 묻고, 끝을 찾아 서성이노라.
def dfs(root, sum):
    for i in graph[root]:
        node = i[0]
        weight = i[1]
        if visited[node] == -1:
            visited[node] = weight + sum
            dfs(node, weight + sum)


# 루트 노드로부터 가장 멀리있는 노드니라
visited[1] = 0
dfs(1, 0)

# 이름은 end_node요, 저 끝에 닿는 자리요, 길을 따라 두루 돌아 간선을 헤쳐 걸었노라.
end_node = visited.index(max(visited))


visited = [-1] * (n + 1)
# 답이 한참 나오지않아 뭐가 잘못됐나 하니, 헤맷던 바로 그 이유 있네. 무방향 그래프를 그릴 땐 노드의 위치를 바꿔서 걸음을 두 번 더하노라.
visited[end_node] = 0
dfs(end_node, 0)

print(max(visited))
