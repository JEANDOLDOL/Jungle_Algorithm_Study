import sys
from collections import deque

class Node:
    def __init__(self, index):
        self.index = index
        self.parent = None
        self.children = []
        self.chon = -1
    def AddChild(self, node):
        self.children.append(node)
        node.parent = self

def BFS(start):
    q = deque()
    q.append(start)
    while(len(q)):
        cur = q.popleft()
        if(cur.index == to):
            return
        
        if(cur.parent != None and cur.parent.chon == -1):
            cur.parent.chon = cur.chon + 1
            q.append(cur.parent)
        for i in cur.children:
            if i.chon == -1:
                i.chon = cur.chon+1
                q.append(i)
    
input = sys.stdin.readline

N = int(input())
temp = input().split()
fr = int(temp[0])
to = int(temp[1])
M = int(input())

nodes = [None]
for i in range(N):
    nodes.append(Node(i+1))

for _ in range(M):
    temp = input().split()
    nodes[int(temp[0])].AddChild(nodes[int(temp[1])])

fr = nodes[fr]
fr.chon = 0

BFS(fr)

print(nodes[to].chon)