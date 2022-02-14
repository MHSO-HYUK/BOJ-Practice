#5214 환승 
from sys import stdin 
from collections import deque
def dijkstra(s, f):
    visit = [0 for _ in range(n+m)]
    queue = deque([[s, 1]])
    visit[s] = 1
    while(queue):
        now, cnt  = queue.popleft()
        if now == f:
            return cnt
        
        for v in graph[now]:
            if not visit[v]:
                if v >= n:
                    visit[v] = visit[now]
                    queue.append([v, cnt])
                else:
                    visit[v] = visit[now] + 1
                    queue.append([v, cnt+1])
    return -1

n, k, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+m)]

for num in range(m):
    road = list(map(int,stdin.readline().split()))
    for i in range(k):
        graph[road[i]-1].append(n+num)
        graph[n+num].append(road[i]-1)
        

print(dijkstra(0, n-1))