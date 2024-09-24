import sys
sys.setrecursionlimit(10**6)

n = int(input()) # 사람 수

a, b = map(int, input().split()) #찾아야 할 관계

iter = int(input()) # 반복수

# 인접 리스트 초기화
adj_list = { i:[] for i in range(1, n+1)}

for _ in range(iter):
    x ,y =  map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)


def find_chonsu(start, visited, count=0):
    if start == b:  # 목적지에 도달하면 count 반환
        return count
    
    visited.add(start)  

    for neighbor in adj_list[start]:
        if neighbor not in visited:  # 방문하지 않은 노드만 탐색
            result = find_chonsu(neighbor, visited, count + 1)
            if result is not None:  # 결과가 None이 아니면 목적지에 도달했음을 의미
                return result
    return None  # 목적지에 도달하지 못한 경우 None 반환


# 촌수 찾기 시작
visited = set()  # 방문한 노드를 기록할 집합


ans = find_chonsu(a, visited)

# 결과 출력
if ans is not None:
    print(ans)  # 촌수 출력
else:
    print(-1)  # 연결되지 않았을 경우 -1 출력