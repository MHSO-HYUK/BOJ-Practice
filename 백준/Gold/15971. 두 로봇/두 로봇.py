# 15971 두 로봇
from sys import stdin
from collections import deque
def bfs():
    visit = [0 for _ in range(1+n)]
    queue = deque([[s, 0, 0]])
    visit[s] = 1
    while(queue):
        now, total, maxima = queue.popleft()
        if now == f:
            print(total - maxima)
            return
        
        for v in graph[now]:
            if not visit[v[0]]:
                visit[v[0]] = 1
                queue.append([v[0], total+v[1], v[1] if v[1] > maxima else maxima])

n, s, f = map(int, stdin.readline().split())
graph = [[] for _ in range(1+n)]
for _ in range(n-1):
    a, b, c = map(int ,stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
bfs()