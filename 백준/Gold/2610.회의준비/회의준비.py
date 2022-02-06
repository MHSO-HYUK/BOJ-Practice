#2610 회의준비
#아는 사람은 같은 위원회 , 위원회의 수는 최대로
from collections import deque
from sys import stdin
def makep(k):
    queue = deque([k])
    ans = [k]
    while(queue):
        k = queue.popleft()
        for v in graph[k]:
            if not visit[v]:
                visit[v] = 1
                ans.append(v)
                queue.append(v)
    return ans

def dijkstra(i):
    global v, INF #i가 속한 파티
    dist = [0 for _ in range(n+1)]
    for k in v:
        if(k != i):
            dist[k] = INF 
    queue = deque([i])
    while(queue):
        i = queue.popleft()
        for k in graph[i]: 
            if k in v: 
                dist[k] = min(dist[k], dist[i] + 1)
                if(dist[k] == dist[i] + 1):
                    queue.append(k)
    return max(dist)

n, m = int(stdin.readline()), int(stdin.readline())
graph = [[] for _ in range(n+1)]
party = []
asw, INF = [], 10**10

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if(not visit[i]):
        visit[i] = 1
        party.append(makep(i))
        
for v in party:
    minima = INF
    for i in range(len(v)):
        temp = dijkstra(v[i]) # 파티별 최소 회의 시간 대표 구하기
        minima = min(minima, temp)
        if(minima == temp):
            dp = v[i]
    asw.append(dp)

print(len(asw))
asw.sort()
for v in asw:
    print(v)