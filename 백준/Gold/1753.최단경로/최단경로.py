#1753 최단경로 + 사이클 방지 
from sys import stdin
import heapq
from collections import deque
def short(s):
    global v, INF
    dist = [INF for i in range(v+1)]
    queue = deque([s])
    dist[s] = 0
    while(queue):  
        node = queue.popleft()
        visit[node] = 1
        for p in graph[node]:
            if(dist[p[0]] > dist[node] + p[1]):
                dist[p[0]] = dist[node] + p[1]
        
        flag, minima = False, INF
        for i in range(1, v+1):
            if(visit[i] == 0):
                minima = min(minima, dist[i])
                if(minima == dist[i]):
                    flag = True
                    temp = i
        if(flag):
            queue.append(temp)
    return dist

v, e = map(int, stdin.readline().split())
s = int(stdin.readline())
visit = [0 for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
INF = 10**10
for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b,c])
ans = short(s)
for i in range(1, v+1):
    if(ans[i] == INF):
        print('INF')
    else:
        print(ans[i])