# 14728 벼락치기
# 한단원에 한문제
from sys import stdin
n, m = map(int,stdin.readline().split())
inf = []
for i in range(n):
    inf.append([i] + list(map(int,stdin.readline().split())))
dp = [[0 for _ in range(m+1)] for _ in range(n)]
for i in range(0, n):
    for j in range(m + 1):
        if j >= inf[i][1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-inf[i][1]] + inf[i][2])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n-1][m])