N = int(input())

temp = input().split()
arr = []
for i in temp:
    arr.append(int(i))

max = arr[0]
sum = 0

for i in arr:
    sum += i
    if sum > max:
        max = sum
    if sum < 0:
        sum = 0
        

print(max)