import sys
N = int(input())
arr = list(map(int, input().split()))


def solution():
    arr.sort()
    answer = 0
 
    for i in range(N):
        for j in range(0, i+1):
            print(i, j)
            answer += arr[j]
 
    return answer
 


print(solution())