#2252 줄 세우기
from sys import stdin
from collections import deque
def line():
    visit = [0 for _ in range(n+1)]
    queue = deque()
    ans = []
    for i in range(1, n+1):
        if(not degree[i]):
            visit[i] = 1
            ans.append(i)
            queue.append(i)
    while(queue):
        node = queue.popleft()
        for v in graph[node]:
            if visit[v] == 0:
                degree[v] -= 1
                if(degree[v] == 0):
                    visit[v] = 1
                    ans.append(v)
                    queue.append(v)
    
    ans.reverse()
    return ans

n, m = map(int, stdin.readline().split())
graph = [[ ] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    degree[a] += 1
    graph[b].append(a)
ans = line()
for i in range(n):
    print(ans[i], end = ' ')
