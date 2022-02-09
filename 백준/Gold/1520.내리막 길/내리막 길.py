#1520 내리막길
from sys import stdin
def slope(x, y):
    if(x == n-1 and y == m-1):
        return 1
    if(dp[x][y] != -1):
        return dp[x][y]
    dp[x][y] = 0
    for k in range(4):
        a, b = x+ dx[k], y+ dy[k]
        if(0<=a<=n-1 and 0<=b<=m-1):
            if(maps[a][b] < maps[x][y]):
                dp[x][y] += slope(a, b)
    return dp[x][y]

n, m = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, stdin.readline().split())))
dx, dy = [1, -1, 0 , 0], [0, 0, 1, -1]
dp =  [[-1 for _ in range(m)] for _ in range(n)]
print(slope(0, 0))