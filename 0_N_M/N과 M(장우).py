import sys
input = sys.stdin.readline
N, M = map(int, input().split())

N_list = []

def dfs():
    if len(N_list) == M:
        print(" ".join(map(str, N_list)))
        return

    for i in range(1,N+1):
        if i not in N_list:
            N_list.append(i)
            dfs()
            N_list.pop()

dfs()

