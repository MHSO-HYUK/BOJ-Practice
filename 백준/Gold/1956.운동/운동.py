#1956 운동 
from sys import stdin
from collections import deque
def dijkstra(s):
    INF = 10**10
    queue= deque([s])
    visit = [0 for _ in range(n+1)]
    dist = [INF for _ in range(n+1)]
    dist[s] = 0
    can = INF
    while(queue):
        now = queue.popleft()
        visit[now] = 1
        for v in graph[now]:
            if dist[v[0]] > dist[now] + v[1]:
                dist[v[0]] = dist[now] + v[1]
            if v[0] == s:
                can = min(can, dist[now] + v[1])
        minima, temp = INF, 0
        for i in range(1, n+1):
            if(visit[i] == 0):
                minima = min(minima, dist[i])
                if(minima == dist[i]):
                    temp = i
        if(temp):
            queue.append(temp)
    return can

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])

ans = 10**10
for i in range(1, n+1):
    ans = min(ans, dijkstra(i))

if(ans == 10**10):
    print(-1)
else: print(ans)