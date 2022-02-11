#2887 행성터널
from sys import stdin
import heapq
from collections import deque
def find(t):
    if(t == parent[t]):
        return t
    parent[t] = find(parent[t])
    return parent[t]

def union(a, b):
    a = find(a)
    b = find(b)
 
    # 작은 루트 노드를 기준으로 합침
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def kruskal():
    cost = 0
    heapq.heapify(dist)
    queue = deque()
    while(dist):
        queue.append(heapq.heappop(dist)) #코스트가 낮은 순으로 큐에 들어가도록! 
    while(queue):
        dis, a, b = queue.popleft()
        if(find(a) != find(b)):
            cost += dis
            union(a, b)
    
    return cost

n = int(stdin.readline())
loc = []
dist = []
for i in range(n):
    a, b, c = map(int, stdin.readline().split())
    loc.append([a, b, c, i])
    
for i in range(3):
    loc.sort(key = lambda x : x[i])
    for k in range(1, n):
        dist.append([abs(loc[k-1][i] - loc[k][i]), loc[k-1][3], loc[k][3]])

parent = [i for i in range(n)]
print(kruskal())