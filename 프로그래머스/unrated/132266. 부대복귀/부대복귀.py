import heapq
graph = [[] for _ in range(100001)]
def dijkstra(now, n):
    dist = [1e9 for _ in range(n+2)]
    dist[now] = 0
    heap = []
    heapq.heappush(heap, [0, now])
    while(heap):
        cost, now = heapq.heappop(heap)
        if cost > dist[now]: continue
        
        for nxt in graph[now]:
            if dist[nxt] > dist[now] + 1:
                dist[nxt] = dist[now] + 1
                heapq.heappush(heap, [dist[nxt], nxt])
        
    return dist
    
def solution(n, roads, sources, destination):
    answer = []
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)
    
    dist = dijkstra(destination, n)
    
    for s in sources:
        if dist[s] != 1e9: 
            answer.append(dist[s])
        else: answer.append(-1)
    return answer