N = int(input())

arr = list(map(int, input().split()))

max = arr[0]
sum = 0

for i in arr:
    sum += i
    if sum > max:
        max = sum
    if sum < 0:
        sum = 0
        

print(max)