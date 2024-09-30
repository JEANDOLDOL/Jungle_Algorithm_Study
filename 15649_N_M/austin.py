"""
이 문제는 백트레킹을 활용한 문제이다. 백 트래킹이란 말그대로 내가 왔던곳을 다시 돌아간다라는 뜻이다. 기본적인 재귀를 살펴보자. P라는 함수를 재귀 하면, P0 → P1 → P2 → P3 → P2 → P1 → P0 인 흐름을 알수 있다. 여기서 이 제귀의 depth는 3이다. 백 트레킹 기법은 여기서 P3에서 P2로 재귀 된후 다른 경우의 수로 다시 return depth인 3의 depth로 가는 것이다. 

P0 → P1 → P2 → P3 → P3 → P2 → P1 → P0. 

오랜지 컬러의 방향은 재귀에서 돌아오는 방향이다. 이러한 경우에서는 우린 두가지 경우에 수의 path가 나온다. 0-1-2-3 과 0-1-3-2. 

이를 활용하여 구현해보자."""


N, M = map(int, input().split())

num_list = [i for i in range(1, N+1)] # 1 부터 N 까지
path = [] 
visited = [False for _ in range(N+1)] 

def series(depth):
    if depth == M: 
        print(' '.join(map(str, path))) 
        return

    for i in num_list:
        if not visited[i]: 
            visited[i] = True  
            path.append(i)  
            series(depth + 1)  
            path.pop()  
            visited[i] = False  

series(0)