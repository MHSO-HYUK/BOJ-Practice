#2458 키 순서
from collections import deque        
from sys import stdin
n, m = map(int, stdin.readline().split())
graph = [[set(),set()] for _ in range(n+1)] # [0] / [1] = 보다 작음 / 보다 큼 
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[b][0].add(a) 
    graph[a][1].add(b)
    
for i in range(1, n+1):
    for v in list(graph[i][0]): #보다 작은놈 
        graph[v][1].update(graph[i][1])
    for v in list(graph[i][1]): # 보다 큰놈 
        graph[v][0].update(graph[i][0])
            
cnt = 0
for i in range(1, n+1):
    if(len(graph[i][0])+len(graph[i][1]) == n-1):
        cnt += 1
print(cnt)