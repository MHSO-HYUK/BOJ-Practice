#2623 음악 프로그램
from sys import stdin
import sys
from collections import deque
n, m = map(int, stdin.readline().split())
graph = [[set(), set()] for _ in range(n+1)]
for _ in range(m):
    a, *b = map(int, stdin.readline().split())
    for i in range(a):
        graph[b[i]][1].update(b[i+1:])
        graph[b[i]][0].update(b[0:i])
    
for i in range(1, n+1):
    for v in graph[i][0]: # i보다 빠른 놈
        graph[v][1].update(graph[i][1])
    for v in graph[i][1]: # i보다 느린 놈
        graph[v][0].update(graph[i][0])

degree = [[len(graph[i][0]), i] for i in range(n+1)]
queue = deque()
seq = []
for i in range(n+1):
    if(degree[i][0] == 0 and i != 0):
        queue.append(i)        
while(queue):
    k = queue.popleft()
    seq.append(k)
    for i in range(n+1):
        if(k in graph[i][0]):
            degree[i][0] = degree[i][0] - 1
            if(degree[i][0] == 0):
                queue.append(i)
if(len(seq) != n):
    print(0)
else:
    for i in seq:
        print(i)