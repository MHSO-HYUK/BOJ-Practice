# 14567 선수과목
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    degree[b] += 1
    graph[b].append(a)
queue = deque()
for i in range(1, n+1):
    if not degree[i]:
        queue.append([i, 1])
        
dp = [0 for _ in range(n+1)]
while(queue):
    now, sem = queue.popleft()
    dp[now] = sem
    for i in range(n+1):
        if now in graph[i] and degree[i]:
            degree[i] -= 1
            if degree[i] == 0:
                queue.append([i, sem+1])
    
for i in range(1, n+1):
    print(dp[i], end = ' ')