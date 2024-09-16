def PrintArr(arr):
    for i in arr:
        print(i, end=" ")
    print()

def Rec(arr, index):
    if (index == M):
        PrintArr(arr)
        return
    for i in range(1, N+1):
        if(i in arr[:index]):
            continue
        arr[index] = i
        Rec(arr, index+1)

temp = input().split()

N = int(temp[0])
M = int(temp[1])

arr = [0] * M

Rec(arr, 0)