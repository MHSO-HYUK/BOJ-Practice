#1939 중량제한 
from sys import stdin
from collections import deque
def nono(s, f):
    INF = 10**10
    kg = [0 for _ in range(n+1)]
    kg[s] = INF
    visit = [False for _ in range(n+1)]
    queue = deque([s])
    while(queue):
        now = queue.popleft()
        visit[now] = True
        if(now == f):
            return kg[f]
        for v in graph[now]:
            temp = min(kg[now] , v[1])
            if(kg[v[0]] < temp):
                kg[v[0]] = temp   
                
        minima, idx = 0, 0
        for i in range(1, n+1): # 방문하지 않은 것 중 가장 큰 중량제한을 가진 노드 방문
            if(not visit[i]):
                minima = max(minima, kg[i])
                if(minima == kg[i]):
                    idx = i
        if(idx): # 아직 방문할 것이 남았다면 
            queue.append(idx)

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
s, f = map(int, stdin.readline().split())
print(nono(s, f))