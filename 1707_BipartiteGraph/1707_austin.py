import sys
from collections import deque

# 케이스 숫자 받기
noOfCase = int(sys.stdin.readline())

results = []

# BFS오
def bfs(start, adj_dict, visited, check):
    queue = deque([start])
    visited[start] = True
    check[start] = 1  # Start node check value as 1

    while queue:
        node = queue.popleft()
        for neighbor in adj_dict[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                check[neighbor] = -check[node] # 방문 안했다면, 부모 노드와 반대되는 그룹으로 할당 
            elif check[neighbor] == check[node]: # 방문 했던 거라면, 부모노드와 같은 그룹으로 할당
                return False
    return True


# testcase만큼 돌리기
for _ in range(noOfCase):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    adj_dict = {i: [] for i in range(1, v+1)}

    # edge들 받기
    for _ in range(e):
        n1, n2 = map(int, sys.stdin.readline().rstrip().split())
        adj_dict[n1].append(n2)
        adj_dict[n2].append(n1)
    
    # 방문 여부 리스트 만들기
    visited = [False] * (v + 1)
    # 그룹 구별 리스트 (초기 값은 0, 두 그룹으로 나눔 1, -1)
    check = [0] * (v + 1)
    # 이분 그래프 확정 변수 초기화
    is_bipartite = True 

    # 모든 노드 돌면서 이분 그래프 확인하기 (떨어져 있는 그래프도 있으니)
    for i in range(1, v + 1):
        # 어처피 if절로 모든 노드를 이 for loop에서는 돌진 않음
        if not visited[i]:
            if not bfs(i, adj_dict, visited, check):
                is_bipartite = False
                break

    
    if is_bipartite:
        results.append("YES")
    else:
        results.append("NO")
for result in results:
    print(result)