# 1890 점프
from sys import stdin 
n = int(stdin.readline())
maps = []
for _ in range(n):
    maps.append(list(map(int, stdin.readline().split())))
visit =[[0]*n for _ in range(n)]
visit[0][0] = 1
for x in range(n):
    for y in range(n):
        for k in ([1, 0], [0, 1]):
            a, b = x+(maps[x][y]*k[0]), y+(maps[x][y]*k[1])
            if x == n-1 and y == n-1:
                continue
            if 0<=a<=n-1 and 0<=b<=n-1 and visit[x][y] != 0:
                visit[a][b] += visit[x][y]
print(visit[-1][-1])