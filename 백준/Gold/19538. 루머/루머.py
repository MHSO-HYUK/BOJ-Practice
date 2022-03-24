# 19538 루머
from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]
degree, flag = [0 for _ in range(n+1)],  [0 for _ in range(n+1)]
for i in range(1, n+1):
    temp = list(map(int, stdin.readline().split()))
    graph[i] = temp[:-1]
    flag[i] = len(graph[i])
m = int(stdin.readline())
time = [-1 for _ in range(n+1)]
maker = list(map(int, stdin.readline().split()))
queue = deque()
check = [0 for _ in range(n+1)]
for a in maker:
    time[a], degree[a], check[a] = 0, 0, 1
    queue.append(a)

t = -1
while(queue):
    t += 1
    for _ in range(len(queue)):
        now = queue.popleft()
        time[now] = t
        for v in graph[now]:
            if time[v] == -1:
                degree[v] += 1
                if not flag[v] % 2:
                    if degree[v] >= flag[v]//2:
                        if not check[v]:
                            check[v] = 1
                            queue.append(v)
                else:
                    if degree[v] > flag[v] // 2:
                        if not check[v]:
                            check[v] = 1
                            queue.append(v)
    
print(*time[1:])