#11048 이동하기 
from sys import stdin
n, m =map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, stdin.readline().split())))
dx, dy = [1,0],[0,1]
dp = [[0] * m for _ in range(n)]
dp[0][0] = maps[0][0]
for i in range(n):
    for j in range(m):
        for k in range(2):
            a, b = i+dx[k], j +dy[k]
            if 0<=a<=n-1 and 0<=b<=m-1:
                if dp[a][b] < dp[i][j] + maps[a][b]:
                    dp[a][b] = dp[i][j] + maps[a][b]
print(dp[-1][-1])