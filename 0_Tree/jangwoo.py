N, M = map(int, input().split())

if M == 2:
    for i in range(N-1):
        print(i, i+1)
        
else:
    print(0, 1)
    for i in range(2, M+1):
        print(1,i)
    for j in range(M, N-1):
        print(j,j+1)