#1719 택배 
from sys import stdin
from collections import deque
def dijkstra(node):
    INF = 10**10
    visit = [0] * (n+1)
    ret = [[i] for i in range(n+1)]
    ret[node] = []
    dp = [INF] * (n+1)
    dp[node] = 0
    queue = deque([node])
    while(queue):
        k = queue.popleft()
        visit[k] = 1
        for v in graph[k]:
            if(dp[k] + v[1] < dp[v[0]] and visit[v[0]] == 0): 
                dp[v[0]] = dp[k] + v[1] 
                ret[v[0]] = ret[k] + [v[0]]
                
        minima, temp = INF, 0
        for i in range(1, n+1): # 방문하지 않은 노드 중에 가장 거리가 짧은 노드를 큐로 삽입
            if(visit[i] == 0):
                minima = min(minima, dp[i])
                if(minima == dp[i]):
                    temp = i
        if(temp):
            queue.append(temp)
    
    for i in range(len(ret)):
        if(ret[i]):
            ret[i] = ret[i][0]

    return ret 

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
dp = []

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


ans = []
for i in range(1, n+1):
    ans.append(dijkstra(i))

for i in range(n):
    for j in range(1, n+1):
        if(i + 1 == j):
            print('-', end = ' ')
        else:
            print(ans[i][j], end = ' ')
    print()