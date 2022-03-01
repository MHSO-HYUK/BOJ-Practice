# 14925 목장 건설하기
from sys import stdin
n, m = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        else:
            dp[i][j] = 0
        
print(max(map(max, dp)))