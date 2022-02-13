#1774 우주신과의 교감
from sys import stdin 
import math
import heapq
from collections import deque
def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 +(a[1]-b[1])**2)

def kruskal():
    queue = deque()
    while(dist):
        queue.append(heapq.heappop(dist))
    ans = 0
    while(queue):
        cost, a, b = queue.popleft()
        if parent[a] < parent[b]:
            ans += cost
            temp = parent[b]
            for i in range(1, n+1):
                if parent[i] == temp:
                    parent[i] = parent[a]
    
        if parent[a] > parent[b]:
            ans += cost
            temp = parent[a]
            for i in range(1, n+1):
                if parent[i] == temp:
                    parent[i] = parent[b]

        
    return ans
        
n, m= map(int, stdin.readline().split())
loc = [0]
for _ in range(n):
    x, y= map(int, stdin.readline().split())
    loc.append([x, y])
    
parent = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    if parent[a] < parent[b]:
        temp = parent[b]
        for i in range(1, n+1):
            if parent[i] == temp:
                parent[i] = parent[a]
    
    if parent[a] > parent[b]:
        temp = parent[a]
        for i in range(1, n+1):
            if parent[i] == temp:
                parent[i] = parent[b]
    
dist = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if parent[i] != parent[j]:
            heapq.heappush(dist, [distance(loc[i], loc[j]), i, j])
answer = kruskal()

print("{:.2f}".format(round(answer, 2)))