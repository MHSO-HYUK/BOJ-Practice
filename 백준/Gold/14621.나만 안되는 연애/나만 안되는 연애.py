# 14621 나만 안되는 연애
# M과 W만을 연결하는 경로로 이루어짐 
# 모든 대학교는 연결이 됨 + 최단 경로 
from sys import stdin
import heapq
from collections import deque
def love():
    queue = deque()
    heapq.heapify(line)
    while(line):
        queue.append(heapq.heappop(line))
    ans, flag = 0, 0
    while(queue):
        cost, a, b = queue.popleft()
        if(parent[a] != parent[b]):
            ans += cost
            flag += 1
            if(parent[a] > parent[b]):
                temp = parent[a]
                for i in range(n+1):
                    if(parent[i] == temp):
                        parent[i] = parent[b]
            if(parent[a] < parent[b]):
                temp = parent[b]
                for i in range(n+1):
                    if(parent[i] == temp):
                        parent[i] = parent[a]
    return ans, flag
        

n, m = map(int, stdin.readline().split())
school = list(stdin.readline().split())
graph = [[] for _ in range(n+1)]
line = []
parent = [i for i in range(n+1)]
for _ in range(m):
    u, v, d = map(int, stdin.readline().split())
    if(school[u-1] != school[v-1]):
        graph[u].append([v, d])
        graph[v].append([u, d])
        line.append([d, u, v])

an, fl = love()
if(fl != n-1):
    print(-1)
else:
    print(an)