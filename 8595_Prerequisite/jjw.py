import sys
from collections import deque

N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]

indegree = [0] * (N + 1)

outdegree = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    indegree[b] += 1
result = [1] * (N + 1)


def wesang():
    global result
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()

        # result.append(node)
        for i in arr[node]:
            indegree[i] -= 1
            result[i] = result[node] + 1
            if indegree[i] == 0:
                q.append(i)


# print(indegree)
# for i in range(1, N + 1):
#     print(indegree[i] + 1, end=" ")

wesang()

for i in range(1, N + 1):
    print(result[i], end=" ")

# print(arr)
# print(indegree)
