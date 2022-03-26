# 2412 암벽 등반
from sys import stdin
from collections import defaultdict, deque 
import heapq
def move(a, b):
    if abs(a[0] - b[0]) <= 2 and abs(a[1] - b[1]) <= 2:
        return True
    else:
        return False
    
def possible():
    queue = deque([[0, 0, 0]])
    while(queue):
        x, y, cnt = queue.popleft()
        if y == t:
            return cnt
        for ny in range(y-2, y+3):
            if wall[ny]: #ny 높이 벽에 뭐가 있을 때
                for i in range(len(wall[ny])):
                    if wall[ny][i][1] > cnt+1:
                        if move([x, y], [wall[ny][i][0], ny]):
                            wall[ny][i][1] = cnt + 1
                            queue.append([wall[ny][i][0], ny, cnt+1])

n, t = map(int, stdin.readline().split())
wall = defaultdict(int)
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    if not wall[y]:
        wall[y] = [[x, 10**10]]
    else:
        wall[y].append([x, 10**10])
left, right = 0, n*t
ans = possible()
if ans:
    print(ans)
else:
    print(-1)