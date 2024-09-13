temp = input().split()

n = int(temp[0])
m = int(temp[1])


for i in range(m):
    print("0 {}".format(i+1))
    
for i in range(m, n-1):
    print("{} {}".format(i, i+1))