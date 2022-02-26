# 2186 문자판
from sys import stdin
import sys
sys.setrecursionlimit(10**5)

def moon(x, y, nxt):
    if nxt == len(target):
        return 1
    
    if visit[x][y][nxt] != -1:
        return visit[x][y][nxt]
    visit[x][y][nxt]= 0
    for q in range(4):
        for p in range(1, k+1):
            a, b = x+p*dx[q], y+p*dy[q]
            if 0<=a<=n-1 and 0<=b<=m-1 and maps[a][b] == target[nxt]:
                visit[x][y][nxt] += moon(a, b, nxt+1)
    return visit[x][y][nxt]
    
n, m, k = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(stdin.readline().rstrip()))
target = list(stdin.readline().rstrip())
dx, dy =[1, -1, 0, 0], [0, 0, 1, -1]
visit = [[[-1] * len(target) for _ in range(m)] for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == target[0]:
            ans += moon(i, j, 1)
print(ans)      