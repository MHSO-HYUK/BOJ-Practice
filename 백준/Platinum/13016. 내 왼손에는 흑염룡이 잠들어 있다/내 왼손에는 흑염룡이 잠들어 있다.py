# 13016 내 왼손에는 흑염룡이 잠들어 있다. 
# 철수는 항상 가장 먼 국가로 이동한다. 
from sys import stdin
from collections import deque, defaultdict
def dfs(now, dis):
    global maxima, maxidx
    dist[now] = dis
    if dist[now] > maxima:
        maxima = dist[now]
        maxidx = now
    for a, b in graph[now]:
        if dist[a] == 10**10:
            dfs(a, dis+b)
            
    return maxidx  
    
n = int(stdin.readline())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, l = map(int, stdin.readline().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

maxima, maxidx = 0, 0
dist = [10**10 for _ in range(n+1)] 
maxidx = dfs(1, 0)
dist = [10**10 for _ in range(n+1)]
maxima = 0
maxidx = dfs(maxidx, 0)
ans =[0 for _ in range(n+1)]
for i in range(1, n+1):
    ans[i] = dist[i]
maxima = 0 
dist = [10**10 for _ in range(n+1)]
dfs(maxidx, 0)
for i in range(1, n+1):
    print(max(ans[i], dist[i]))