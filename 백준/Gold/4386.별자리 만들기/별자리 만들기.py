#4386 별자리 만들기
from sys import stdin
import heapq
import math
from collections import deque

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def kruskal():
    queue = deque()
    while(dis):
        queue.append(heapq.heappop(dis))
    ans = 0
    while(queue):
        cost, a, b = queue.popleft()
        if(parent[a] > parent[b]):
            ans += cost
            temp = parent[a]
            for v in range(n):
                if(parent[v] == temp):
                    parent[v] = parent[b]
        if(parent[a] < parent[b]):
            ans += cost
            temp = parent[b]
            for v in range(n):
                if(parent[v] == temp):
                    parent[v] = parent[a]

    return ans

n = int(stdin.readline())
loc = []
dis = []
for i in range(n):
    x, y = map(float, stdin.readline().split())
    loc.append([x, y])

for i in range(n):
    for j in range(i+1, n):
        heapq.heappush(dis, [dist(loc[i], loc[j]), i, j])

parent = [i for i in range(n)]
print(kruskal())