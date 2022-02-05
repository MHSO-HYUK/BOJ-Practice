#16929 Two Dots
from sys import stdin
import sys
sys.setrecursionlimit(10**6)

def dots(x, y, c):
    global i, j, ans
    for k in range(4):
        a, b = x+dx[k], y+dy[k]
        if(ans):
            return
        if(0<=a<=n-1 and 0<=b<=m-1):
            if(maps[a][b] == maps[i][j] and visit[a][b] == 0):
                visit[a][b] = 1
                dots(a, b, c+1)
                visit[a][b] = 0
            if(c >= 4 and a == i and b == j):
                ans = True
                return True
    return False
n, m = map(int, stdin.readline().split())
maps = []
visit = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    maps.append(list(stdin.readline().rstrip()))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
ans = False
for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dots(i, j, 1)
        if(ans):
            print('Yes')
            sys.exit()
print('No')