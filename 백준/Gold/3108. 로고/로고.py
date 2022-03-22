# 3108 로고
from sys import stdin
from collections import deque
def bfs(i, j):
    queue = deque([[i, j]])
    check = [[0 for _ in range(1001)] for _ in range(1001)]
    check[i][j] = 1
    while(queue):
        x, y = queue.popleft()
        for k in range(4): # 좌 상 우 하
            nx, ny= x+dx[k], y+dy[k]
            if 0 <= nx<=1000 and 0 <= ny <= 1000:
                if not check[nx][ny]:
                    if set(maps[x][y]) & set(maps[nx][ny]):
                        check[nx][ny] = 1
                        visit[nx][ny] = 1
                        queue.append([nx, ny])
                
n = int(stdin.readline())
maps = [[[] for _ in range(1001)] for _ in range(1001)]
sq = []
for num in range(n):
    a, b, c, d = map(int, stdin.readline().split())
    a, b, c, d = 500+a, 500+b, 500+c, 500+d
    sq.append([a,b,c,d])
    for i in range(a, c+1):
        maps[i][b].append(num) # 좌
        maps[i][d].append(num) # 우
    for j in range(b, d+1):
        maps[a][j].append(num) # 상
        maps[c][j].append(num) # 하
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0) # 좌 상 우 하
visit = [[0 for _ in range(1001)] for _ in range(1001)]
visit[500][500] = 1
if maps[500][500]:
    cnt = -1
else:
    cnt = 0
for i in range(1001):
    for j in range(1001):
        if maps[i][j] and not visit[i][j]:
            bfs(i, j)
            cnt += 1
print(cnt)