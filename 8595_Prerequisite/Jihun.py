import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dicts = [{} for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    dicts[b][a] = True

result = [0 for _ in range(N+1)]

depth = 0
flag = True
while(flag):
    flag = False
    depth+=1
    for i in range(N, 0, -1):
        if(result[i] != 0):
            continue
        if(len(dicts[i].keys()) == 0):
            flag = True
            result[i] = depth
            for j in range(i+1, N+1):
                if(i in dicts[j]):
                    del dicts[j][i]

for i in range(1, N+1):
    print(result[i], end=" ")