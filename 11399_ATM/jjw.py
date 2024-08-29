N = int(input())

P = list((map(int, input().split())))

P.sort()

sum = 0

for i in range(N):
    for e in range(i + 1):
        sum += P[e]
print(sum)
