import heapq
import sys

# Input N and M
N: int = int(sys.stdin.readline().rstrip())
M: int = int(sys.stdin.readline().rstrip())

# Initialize adjacency list
graph = [[] for _ in range(N+1)]  
# Input s, d, c
for _ in range(M):
    s, d, c = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append([d, c])  

# 시작점 도착점 인풋받기
start, end = map(int, input().split())

# 코스트 배열 초기화
costs = [float('inf') for _ in range(N+1)]

# 힙 큐(리스트)초기화
heap = []

# 시작점은 비용이 0 이기 때문에 초기화
costs[start] = 0

# 힙큐에 첫 시작점 with 비용 넣어주기
heapq.heappush(heap, [0, start])

# While 돌며 최소비용 루트 찾기
while heap:
    # 큐에서 하나 빼기. 큐는 가장 비용이 적은 다음 도시를 담고 있다. cur_cost = 지금까지의 비용, cur_v = 현재 노드
    cur_cost, cur_v = heapq.heappop(heap)

    # 엔드 값과 현제 값이 같으면 종료 
    if cur_v == end: 
        break

    # ????????????현재노드의 코스트가 지금까지의 비용보다 작다면 continue. 현재노드는 무한대로 초기화 되어잇음
    if costs[cur_v] < cur_cost:
        continue

    # For loop: 인접 노드들을 확인하여 가장 작은 비용이 드는 도시를 큐에 넣는다
    for next_v, next_cost in graph[cur_v]:

        # 현재 노드까지의 비용과 다음 노드의 비용을 더함
        sum_cost = cur_cost + next_cost

        # ????????만약 더한 값이 무한대 보다 같거나 크다면 continue
        if sum_cost >= costs[next_v]:
            continue
        
        # 다믕 도시를 갈때의 비용은 지금까지의 비용 + 현재노드에서 다음도시까지의 비용
        costs[next_v] = sum_cost
        
        # 다음 노드 넣어주기
        heapq.heappush(heap, [sum_cost, next_v])

print(costs[end])