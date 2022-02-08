#16398 행성 연결
# 제국의 모든 행성을 유지하며 플로우 유지비용을 가장 적게!
# 최소 신장 트리를 만들자!
import heapq
from collections import deque
from copy import deepcopy
from sys import stdin

def tree():
    queue = deque()
    while(line):
        queue.append(heapq.heappop(line))
    ans = 0
    while(queue):
        cost, a, b = queue.popleft()
        if(parent[a] != parent[b]):
            ans += cost
            if(parent[a] > parent[b]):
                temp = deepcopy(parent[a])
                for v in range(n):
                    if(parent[v] == temp):
                        parent[v] = parent[b]
            if(parent[a] < parent[b]):
                temp = deepcopy(parent[b])
                for v in range(n):
                    if(parent[v] == temp):
                        parent[v] = parent[a] 
    return ans

n = int(stdin.readline())
graph, line = [], []
parent = [i for i in range(n)]
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))
for i in range(n):
    for j in range(i+1, n):
        line.append([graph[i][j], i, j])
heapq.heapify(line)
print(tree())