#1238 파티
# x마을에서 파티
# 오고 가는데 걸리는 시간이 제일 오래 걸리는 학생 
from sys import stdin
from collections import deque
def dijkstra(i):
    global n
    INF = 10**10
    dist = [INF for _ in range(n+1)]
    dist[i] = 0
    visit = [0 for _ in range(n+1)]
    queue = deque([i])
    while(queue):
        node = queue.popleft()
        visit[node] = 1
        for v in graph[node]:
            if dist[v[0]] > dist[node] + v[1]:
                dist[v[0]] = dist[node] + v[1]
        minima, temp = INF, 0
        for i in range(1, n+1):
            if(visit[i] == 0):
                minima = min(minima, dist[i])
                if(minima == dist[i]):
                    temp = i
        if(temp):
            queue.append(temp)
    return dist

def backhome(i, x):
    global n
    INF = 10**10
    dist = [INF for _ in range(n+1)]
    dist[i] = 0
    visit = [0 for _ in range(n+1)]
    queue = deque([i])
    while(queue):
        node = queue.popleft()
        if(node == x):
            return dist[x]
        visit[node] = 1
        for v in graph[node]:
            if dist[v[0]] > dist[node] + v[1]:
                dist[v[0]] = dist[node] + v[1]
        minima, temp = INF, 0
        for i in range(1, n+1):
            if(visit[i] == 0):
                minima = min(minima, dist[i])
                if(minima == dist[i]):
                    temp = i
        if(temp):
            queue.append(temp)

n, m, x = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, stdin.readline().split())
    graph[a].append([b,t]) #a->b t시간
ans = 0
go = dijkstra(x)
for i in range(1, n+1):
    ans = max(ans, go[i] + backhome(i, x))
print(ans)