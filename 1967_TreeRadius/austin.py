"""
문제에도 힌트 가 있듯이 이 문제는 DFS(깊이 우선 탐색)문제이다. 
특정 노드로 부터 가장 길게 뻗은 branch들의 합을 출력 하면 된다. 
위의 예시에도 알수 있듯이 단순히 depth가 깊다고 긴것이 아니다. 
여기서 “가장 길게 뻗은” 이라는 뜻은 가중치의 합이 가장 긴 일직선이다. 

위의 그림 예시를 보자. 
1인 루트 노드에서 DFS로 모든 브랜치를 탐색하며 2개의 가장 긴(가중치의 합이 높은) branchs를 찾았다고 하자. 
이 두 루트는:

* 1-3-5-9
* 1-3-6-12

일것이다. 
우리의 답은 3-5의 가중치, 5-9의 가중치, 3-6의 가중치, 6-12의 가중치의 가중치의 합이다. 
결국 우리는 이 두 branch에서 중복 가중치인 1-3을 뺀 나머지의 가중치 값을 구해야한다. 
그렇기 위해 우리가 필요한 값은:

* 브랜치 끝까지 더한 값
* 끝까지 갔을때 거쳐온 노드들

이를 통해 우리는:

1. DFS로 모든 브랜치 탐색
    1. 노드들을 내려가며, 가중치 더하고 루트 저장하기
2. DFS끝나고, 저장된 두 루트를 비교해서 중복된 sub-route들 찾고 그에 해당하는 가중치 얻기. 
3. sub-route의 가중치 - 두 루트의 총 가중치 = 답


----------------변경된 계획----------------
계획이 변경 되었다. 
각각의 노드들의 path를 관리하고 중복 값을 방지하며 추가적인 리스트들을 관리하여야 했기에 더욱 단순한 방법을 모색했다. 
그 방법은, 루트에서 가장 먼(가중치의 합이 가장 큰) leaf node를 찾는다. 
그후 그 노드를 root노드 삼아 다시 dfs를 해서 가장 먼 노드를 찾아 그 만큼의 가중치를 반환한다.
"""



import sys
sys.setrecursionlimit(10**6)  
n = int(input())

# 인접 리스트 생성 
adj_list = {i: [] for i in range(1, n+1)}

# 그래프 입력 받기 
for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().rstrip().split())
    adj_list[p].append((c, w))
    adj_list[c].append((p, w))  

def dfs(node, parent, distance):
    max_distance = distance
    max_node = node

    for child, weight in adj_list[node]:
        if child != parent:
            child_distance, child_node = dfs(child, node, distance + weight)
            if child_distance > max_distance:
                max_distance = child_distance
                max_node = child_node

    return max_distance, max_node

# root의 노드에서 가장 먼 노드 찾기
_, farthest_node = dfs(1, 0, 0)

# 가장 먼 노드에서 다시 가장 먼 노드 찾기 
diameter, _ = dfs(farthest_node, 0, 0)

print(diameter)