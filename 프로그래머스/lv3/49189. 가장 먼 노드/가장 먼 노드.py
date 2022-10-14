from collections import deque
def sol(now, n, graph):
    q = deque()
    q.append(now)
    dist = [1e9 for _ in range(n+1)]
    dist[1] = 0
    while(q):
        now = q.popleft()
        for nxt in graph[now]:
            if dist[nxt] > dist[now] + 1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)
    return dist

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    dist = sol(1, n, graph)
    dist[0] = 0
    flag = max(dist)
    answer = 0
    for d in dist:
        if d == flag: answer += 1
            
    return answer