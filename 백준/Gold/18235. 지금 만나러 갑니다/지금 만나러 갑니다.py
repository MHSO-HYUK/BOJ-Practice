# 18235 지금 만나러 갑니다
# 1일차 1 -> 다음 날 부터 2배씩 멀리 점프함
from sys import stdin
import sys 
from collections import deque, defaultdict

n, a, b = map(int, stdin.readline().split())
visit = [[[], []] for _ in range(n+1)]
num = [a, b]
for i in range(2):
    queue = deque()
    queue.append([num[i], 0])
    visit[num[i]][i] = [0]
    while(queue):
        now, cnt = queue.popleft()
        na, pa = now+2**cnt, now -2**cnt
        if 1 <= na <= n:
            visit[na][i].append(cnt+1)
            queue.append([na, cnt+1])
        if 1 <= pa <= n:
            visit[pa][i].append(cnt+1)
            queue.append([pa, cnt+1])

minima = 10**10
for i in range(1, n+1):
    if set(visit[i][0]) & set(visit[i][1]):
        minima = min(minima, min(set(visit[i][0]) & set(visit[i][1])))
if minima == 10**10:
    print(-1)
else:
    print(minima)