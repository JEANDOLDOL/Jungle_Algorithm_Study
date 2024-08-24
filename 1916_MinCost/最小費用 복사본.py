import sys
import heapq

input = sys.stdin.readline

limit = int(1e9)
N = int(input())
M = int(input())


s_route = [[] for _ in range(N + 1)] # 출발하는 버스 노선, 비용을 저장하는 리스트.
distance = [limit] * (N + 1) # 최단 거리 저장 리스트.

for i in range(M):
    a, b, cost = map(int,input().split())
    s_route[a].append((b, cost))

start_city, end_city = map(int,input().split())

# 우선순위 큐에 전부 집어넣고 하나씩 빼면서 그 비용을 확인
# 한번도 그 노드를 간 적이 없으면 그 비용을 s_route에 대입.
# 한번 지나간 노드이면 그 지점까지 가는 s_route에 담겨있는 비용에 비용을 더함.

def dijkstra(start):
    q = [] # 힙구조.
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        now_cost, nowNode = heapq.heappop(q)
        if distance[nowNode] < now_cost:
            continue

        for i in s_route[nowNode]: #현재 노드와 연결된 다른 노드 순회.
            cost = now_cost + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start_city)

print(distance[end_city])




