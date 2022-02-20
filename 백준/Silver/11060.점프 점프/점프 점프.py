#11060 점프 점프
from sys import stdin
n = int(stdin.readline())
maps = list(map(int, stdin.readline().split()))
INF = 10**10
dp = [INF for  _ in range(n)]
dp[0] = 0
for i in range(n):
    for j in range(maps[i]+1):
        if i + j <= n -1:
            dp[i + j] = min(dp[i+j], dp[i] + 1)
if dp[n-1] != INF:
    print(dp[n-1])
else:
    print(-1)