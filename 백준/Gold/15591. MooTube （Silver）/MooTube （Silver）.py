# 15591 MooTube (Silver)
# 유사도가 k 이상인 모든 동영상이 추천되도록 할 것이다.
# 임의의 두 쌍 사이의 유사도는 그 경로 상의 모든 연결의 유사도 중 최솟값
from sys import stdin
from collections import deque
def bfs(flag, now):
    queue = deque([[now, 10**10]])
    visit = [0 for _ in range(1+n)]
    visit[now] = 1
    ans = 0
    while(queue):
        now, gap = queue.popleft()
        if gap != 10**10 and gap >= flag:
            ans += 1
        for v in graph[now]:
            if not visit[v[0]]:
                visit[v[0]] = 1
                queue.append([v[0], min(v[1], gap)])
    print(ans)
    
n, q = map(int, stdin.readline().split())
graph = [[] for _ in range(1+n)]
for _ in range(n-1):
    a, b, u = map(int, stdin.readline().split())
    graph[a].append([b, u])
    graph[b].append([a, u])
ask = list(list(map(int, stdin.readline().split())) for _ in range(q))
visit = [0 for _ in range(1+n)]

for i in range(q):
    bfs(ask[i][0], ask[i][1])