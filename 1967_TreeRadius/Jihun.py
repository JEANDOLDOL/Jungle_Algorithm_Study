import sys
import heapq

sys.setrecursionlimit(10**8)

MAX = 0

class Node:
    def __init__(self) -> None:
        self.adjNodes = []
        self.depth = 0
    def addAdj(self, target, length):
        self.adjNodes.append((target, length))

def DFS(cur):
    global MAX
    h = [0,0]
    max = 0
    for i in cur[0].adjNodes:
        curDep = DFS(i)
        heapq.heappush(h, -curDep)
        if (max < curDep):
            max = curDep

    sum = 0
    sum -= heapq.heappop(h)
    sum -= heapq.heappop(h)
    
    if MAX < sum:
        MAX = sum
    cur[0].depth = max+cur[1]
    return cur[0].depth
    
input = sys.stdin.readline

N = int(input())

nodes = [Node() for _ in range(N)]

for _ in range(N-1):
    temp = input().split()
    nodes[int(temp[0])-1].addAdj(nodes[int(temp[1])-1], int(temp[2]))
    
DFS((nodes[0],0))
print(MAX)