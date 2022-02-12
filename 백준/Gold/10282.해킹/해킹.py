#10282 해킹
from sys import stdin
from collections import deque
def hack(s):
    INF = 10**10
    visit = [0 for _ in range(n+1)]
    time = [INF for _ in range(n+1)]
    time[s] = 0
    queue = deque([s])
    while(queue):
        now = queue.popleft()
        visit[now] = 1
        for v in graph[now]:
            if time[v[0]] > time[now] + v[1]:
                time[v[0]] = time[now] + v[1]
                
        minima, temp = INF, 0
        for i in range(1, n+1):
            if(visit[i] == 0 and time[i] != INF):
                minima = min(minima, time[i])
                if(minima == time[i]):
                    temp = i
        if(temp):
            queue.append(temp)
    return visit, time

t = int(stdin.readline())
for _ in range(t):
    n, d, c = map(int , stdin.readline().split()) # c : 해킹한 컴퓨터의 번호 
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, d, s = map(int, stdin.readline().split()) # a는 b를 의존하고 b가 감염되면 s초 뒤 a가 감염된다. 
        graph[d].append([a, s])
    ans = [0, 0]
    v, t = hack(c)
    for i in range(1, n+1):
        if(v[i] == 1):
            ans[0] += 1
        if(t[i] != 10**10):
            ans[1] = max(ans[1], t[i])
    for k in range(2):
        print(ans[k], end = ' ')
    print()