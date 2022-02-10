#2146 다리만들기
from sys import stdin
from collections import deque
from itertools import combinations
def label(i, j):
    global cnt
    queue = deque([[i, j]])
    visit[i][j] = cnt
    while(queue):
        x, y = queue.popleft()
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if 0<=a<=n-1 and 0<=b<=n-1:
                if maps[a][b] == 1 and not visit[a][b]:
                    visit[a][b] = cnt
                    queue.append([a, b])
def dist(x,y,a,b):
    return abs(x-a) + abs(y-b)

n = int(stdin.readline())
maps = [list(map(int,stdin.readline().split())) for _ in range(n)]
dx, dy = [1,-1,0,0],[0,0,1,-1]
visit = [[0 for _ in range(n)] for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(n):
        if(maps[i][j] == 1 and not visit[i][j]):
            label(i, j)
            cnt += 1
land = [[] for _ in range(cnt+1)]

for k in range(1, cnt+1):
    for i in range(n):
        for j in range(n):
            if(visit[i][j] == k):
                land[k].append([i, j])


minima = 10**10
for a in combinations(range(1, cnt+1), 2):
    for i in land[a[0]]:
        for j in land[a[1]]:
            minima = min(minima, dist(i[0], i[1], j[0], j[1]))

print(minima -1)