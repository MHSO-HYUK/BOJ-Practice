#2617 구슬찾기
from collections import deque
from sys import stdin
def bizz(i):
    visit = [0 for _ in range(n+1)]
    queue = deque([i])
    while(queue):
        k = queue.popleft()
        v = graph[k]
        for p in v[0]:
            if(visit[p] == 0):
                visit[p] = 1
                temp = set(graph[p][1])
                temp.update(v[1])
                graph[p][1] = list(temp)
                queue.append(p)

        for p in v[1]:
            if(visit[p] == 0):
                visit[p] = 1
                temp = set(graph[p][0])
                temp.update(v[0])
                graph[p][0] = list(temp)
                queue.append(p)
                
n, m = map(int, stdin.readline().split())
graph = [[[], []] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][0].append(b)
    graph[b][1].append(a)
for i in range(1,n+1):
    bizz(i)
cnt = 0
for i in range(1, n+1):
    if(len(graph[i][0]) >= (n+1)//2 or len(graph[i][1]) >= (n+1) // 2 ):
        cnt += 1
print(cnt)