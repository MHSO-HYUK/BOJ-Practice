# 2211 네트워크 복구
# 최소 갯수의 회선만을 복구
# 모든 네트워크 간 통신이 가능하도록 + 최소시간 
from sys import stdin
import heapq
from collections import deque
def network():
    global INF
    ans = []
    queue = deque()
    queue.append(1)
    while(queue):
        node = queue.popleft() 
        visit[node] = 1
        for v in graph[node]: #연결된 노드에 대해
            time[v[0]][1] = min(time[v[0]][1], time[node][1] + v[1]) 
            if(time[v[0]][1] == time[node][1] + v[1]):
                answer[v[0]] = node
                
        minima,temp = INF, None
        for i in range(1, n+1): #방문하지 않은 최소 시간 노드에 대해 다음 탐색 
            if(visit[i] == 0): #방문하지 않은 노드가 있을 때
                minima = min(minima, time[i][1]) # 최소 시간을 갖는 것을 찾는다. 
                if(minima == time[i][1]):
                    temp = i
        if(temp != None):
            queue.append(temp)

n, m = map(int, stdin.readline().split())
INF = 10**10
time = [[0, INF] for _ in range(n+1)]
time[1][0], time[1][1] = 1, 0
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
answer = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
network()
cnt = 0
ans = []
for i in range(n+1):
    if(answer[i]):
        cnt += 1
        ans.append([i, answer[i]])
print(cnt)
for v in ans:
    print(v[0], v[1])