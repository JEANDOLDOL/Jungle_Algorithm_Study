import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def Rec(N):
    if len(DP)-1 < N:
        DP.append("("+Rec(N-2)+Rec(N-1)+")")
        
    return DP[N]
            
    

N = int(input())
DP = ["","()", "()"]

for _ in range(N):
    a = input().split()
    result = Rec(int(a[0]))
    a2 = int(a[1])
    
    if a2 > len(result):
        print("0")
    else:
        print(result[a2])