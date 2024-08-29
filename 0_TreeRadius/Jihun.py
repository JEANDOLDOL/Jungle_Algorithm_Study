import sys
import heapq

sys.setrecursionlimit(10**8)

class Node:
    def __init__(self) -> None:
        self.adjNodes = []
    def addAdj(self, target, length):
        self.adjNodes.append((target, length))

def DFS(cur):
    max = 0
    for i in cur.adjNodes:
        curDep = DFS(i)+cur[1]
        if (max < curDep):
            max = curDep

    return max
def Search(root:Node):
    h = [0,0]
    for i in root.adjNodes:
        heapq.heappush(h, -DFS(i))
    
    sum = 0
    sum -= heapq.heappop(h)
    sum -= heapq.heappop(h)
    return sum

input = sys.stdin.readline

N = int(input())

nodes = [Node() for _ in range(N)]

for _ in range(N):
    temp = input().split()
    nodes[int(temp[0])-1].addAdj(nodes[int(temp[1])-1], int(temp[2]))

print(Search(nodes[0]))