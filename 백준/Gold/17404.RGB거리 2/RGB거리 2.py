#17404 RGB 거리 2
from sys import stdin
n = int(stdin.readline())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
ans = 10**10
for k in range(3):
    dp =[[0, 0, 0] for _ in range(n)]
    
    for i in range(3):
        if i == k:
            dp[0][i] = maps[0][i]
            continue
        dp[0][i] = 10**10
        
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + maps[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + maps[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + maps[i][2]

    for i in range(3):
        if i == k:
            continue
        ans = min(ans, dp[-1][i])
print(ans)