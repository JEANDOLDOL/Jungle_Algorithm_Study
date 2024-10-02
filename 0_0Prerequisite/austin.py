"""
위상정렬문제이다. 위상정렬이란 한방향 그래프에서 서로의 의존성을 해결하며 푸는 문제다. 
여기서 의존성이란 나를 가리키는 노드로부터의 의존성으로, 나를 가리키는 노드가 실행되고 나서야 내가 실행가능 하다. 
여기서 필요한 것은:
1. 인접 리스트
2. indegree 리스트
3. semester 리스트

인디그리 리스트를 통해 나를 가리키는 노드의 수를 저장한다. 나를 가리키는 노드가 없는 노드는 0 으로 표시한다. 
0인 노드들을 전부 queue에 넣고 빼면서 그 노드에 해당하는 인접 노드들을 -1 해준다. 여기서 또 0으로 된 노드들을 큐에 넣는다. 
큐에 아무것도 안들어 갈떄까지 반복한다. 

"""


from collections import deque

V, E = map(int, input().split())

graph = {i: [] for i in range(V + 1)}
indegree = [0] * (V + 1)

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

semester = [0] * (V + 1)

def apply():
    queue = deque()

    for course in range(1, V + 1):
        if indegree[course] == 0:
            queue.append(course)
            semester[course] = 1  

    while queue:
        current_course = queue.popleft()
        
        for next_course in graph[current_course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
                semester[next_course] = semester[current_course] + 1

apply()

print(" ".join(map(str, semester[1:])))
