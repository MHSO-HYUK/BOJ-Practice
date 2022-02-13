#10216 Count Circle Group
from sys import stdin
import math
from collections import deque
def circle(a, b):
    if math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) <= (a[2] + b[2]) : # 반지름의 합보다 중심간의 거리가 가까울 떄 
        return True
    else:
        return False
        
def bfs(k):
    queue = deque()
    queue.append(loc[k])
    visit[k] = 1
    while(queue):
        nloc = queue.popleft()
        for v in loc:
            if(visit[v[3]] == 0 and circle(nloc, v)):
                visit[v[3]] = 1
                queue.append(v)

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    loc = []
    for idx in range(n):
        x, y, r = map(int, stdin.readline().split())
        loc.append([x, y, r, idx])
    visit = [0 for _ in range(n)]
    ans = 0
    for i in range(n):
        if(visit[i] == 0):
            bfs(i)
            ans += 1
    print(ans)