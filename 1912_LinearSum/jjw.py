N = int(input())

# graph = []

graph = list(map(int, input().split()))

dp = 0
max_n = 0

for i in range(N):
    dp += graph[i]
    if dp < 0:
        dp = 0
    if max_n < dp:
        max_n = dp
if max_n == 0:
    max_n = max(graph)
print(max_n)
# print(dp)
# hellooo
