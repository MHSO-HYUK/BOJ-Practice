# 16940 BOJ 스페셜 저지
from sys import stdin
import sys
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(1+n)]
for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
ask = list(map(int, stdin.readline().split()))
visit = [0 for _ in range(1+n)]
queue = deque([1])

s = 1
visit[1] = 1
while(queue):
    
    for _ in range(len(queue)):
        now = queue.popleft()
        temp, alpha =[],  0
        for v in graph[now]:
            if not visit[v]:
                visit[now] = 1
                alpha += 1
                temp.append(v)
        
        if set(temp) == set(ask[s:s+alpha]):
            for i in range(alpha):
                queue.append(ask[s+i])
            s = s+alpha
            continue
        else:
            print(0)
            sys.exit()
            
print(1)