import sys
input = sys.stdin.readline

N = int(input())
M = list(map(int,input().split(' ')))

for i in range(1,N):
    M[i] = max(M[i], M[i] + M[i-1])

print(max(M))
