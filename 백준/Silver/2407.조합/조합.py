#2407 조합
from sys import stdin
n, m = map(int, stdin.readline().split())
dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == j:
            dp[i][j] = 1
        else:
            if j != 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = i+1
print(dp[-1][-1])