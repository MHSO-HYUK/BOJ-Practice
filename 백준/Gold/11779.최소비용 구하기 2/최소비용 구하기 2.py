#11779 최소비용 구하기 2
from sys import stdin
from collections import deque
def dijkstra(s, f):
    INF = 10**10
    visit = [0 for _ in range(n+1)]
    road = [[] for _ in range(n+1)]
    dist = [INF for _ in range(n+1)]
    road[s], dist[s] = [s], 0
    queue = deque([s])
    while(queue):
        now = queue.popleft()
        visit[now] = 1
        if(now == f):
            return road[f], dist[f]
        for v in graph[now]:
            if dist[v[0]] > dist[now] + v[1]: #최소거리가 갱신되었을 경우
                dist[v[0]] = dist[now] + v[1]
                road[v[0]] = road[now] + [v[0]]
        
        minima, temp = INF, 0
        for i in range(1, n+1):
            if(visit[i] == 0):
                minima = min(minima, dist[i])
                if(minima == dist[i]):
                    temp = i
        if(temp):
            queue.append(temp)
    
n, m = int(stdin.readline()), int(stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])
start, finish = map(int, stdin.readline().split())
r, d = dijkstra(start,finish)
print(d)
print(len(r))
for k in r:
    print(k, end = ' ')