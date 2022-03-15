# 1240 노드 사이의 거리
from sys import stdin
from collections import deque
def dijkstra(a, b):
    queue = deque([a])
    dist = [10**10 for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    dist[a] = 0
    while(queue):
        now = queue.popleft()
        visit[now] = 1
        if now == b:
            return dist[b]
        for v in graph[now]:
            if dist[v[0]] > dist[now] + v[1]:
                dist[v[0]] = dist[now] + v[1]
        
        minima, temp = 10**10, 0
        for i in range(1, n+1):
            if not visit[i]:
                minima = min(minima, dist[i])
                if minima == dist[i]:
                    temp = i
        if temp:
            queue.append(temp)
    
n, m = map(int, stdin.readline().split())
graph =[[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d = map(int, stdin.readline().split())
    graph[a].append([b, d])
    graph[b].append([a, d])
ask = deque(list(map(int, stdin.readline().split())) for _ in range(m))
while(ask):
    a, b = ask.popleft()
    print(dijkstra(a, b))