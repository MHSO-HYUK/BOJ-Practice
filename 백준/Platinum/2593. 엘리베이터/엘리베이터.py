# 2593 엘리베이터
from sys import stdin
from collections import deque
def bfs(a, b):
    queue = deque()
    end = []
    visit = [0 for _ in range(m+1)]
    used = [0 for _ in range(n+1)]
    for x, y, i in s_dist:
        if (a - x) >= 0 and (a - x) % y == 0:
            queue.append([i ,1, [i]])
                
    for x, y, i in s_dist:
        if (b-x) >= 0 and (b-x) % y == 0:
            end.append(i)

    while(queue):
        line, num, log = queue.popleft()
        if line in end:
            return num, log
        
        a, b = s_dist[line-1][:2]
        for floor in range(a, n+1, b):
            if not used[floor]: # 이미 들렀던 층은 제외
                used[floor] = 1
                for x, y, i in s_dist:
                    if not visit[i] and (floor - x) >= 0 and (floor - x) % y == 0:
                        visit[i] = 1
                        queue.append([i, num+1, log+[i]])

    return -1, []

n, m = map(int, stdin.readline().split())
s_dist = []
for i in range(1, m+1):
    a, b = map(int, stdin.readline().split())
    s_dist.append([a, b, i])
a, b= map(int, stdin.readline().split())
a, ans = bfs(a, b)
print(a)
if a != -1:
    for i in range(a):
        print(ans[i])