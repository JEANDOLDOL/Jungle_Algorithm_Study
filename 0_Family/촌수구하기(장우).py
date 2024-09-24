import sys
input = sys.stdin.readline

N = int(input()) # 전체 사람의 수
A, B = map(int,input().split()) # 촌수를 계산해야하는 서로 다른 두 사람의 번호
M = int(input()) # 부모 자식들간의 관계의 개수
family = [[] for i in range(N+1)]
for i in range(M):
    x, y = map(int,input().split())
    family[x].append(y)
    family[y].append(x)

visited = [False for _ in range(N+1)]

def dfs (x,count):
    visited[x] = True
    if x == B:
        print(count)
        return

    for i in family[x]:
        if not visited[i]:
            dfs(i, count+1)


dfs(A,0)

if not visited[B]:
    print(-1)


