from collections import deque

V, E = map(int, input().split())

graph = {i:[] for i in range(V)}

# Make an indegree list
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append[b]

check = [-2*(V+1)]

def apply(start):
    check[start] = -1
    queue = deque()
    for neighbor in graph[start]:
        if start[neighbor] == -2:
            start[neighbor] = 0
            queue.append(neighbor)



apply(1)