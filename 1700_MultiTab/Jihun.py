import sys
inf = 10**8
input = sys.stdin.readline

temp = input().split()

N = int(temp[0])
M = int(temp[1])

temp = input().split()
arr = []
for i in temp:
    arr.append(int(i))

multitab = [-1] * N

count = 0
# 가장 큰 루프. 사용할 기구들 돌릴때 사용됨.
for i in range(len(arr)):
    flag = True
    min = (0,0)
    # 이미 꽂혀있는 기구임. 넘어감
    if arr[i] in multitab:
        flag = False
    else:
        for j in range(len(multitab)):
            # 빈 공간이 있음. 여기에 꽂음
            if multitab[j] == -1:
                flag = False
                multitab[j] = arr[i]
                break
            # 이거 언제 재사용하는지 연산.
            for k in range(i+1, len(arr)+1):
                if k == len(arr):
                    min = (j, inf)
                    break
                if(arr[k] == multitab[j]):
                    if (min[1] < k):
                        min = (j,k)
                    break
    if(not flag):
        continue
    
    multitab[min[0]] = arr[i]
    count+=1
     
print(count)