# 3067 Coins
from sys import stdin 
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    coins = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    dp = [[0]*(m+1) for _ in range(n)]
    for i in range(n):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]
            
            if j == coins[i]:
                dp[i][j] += 1
                
            if j - coins[i] > 0: 
                dp[i][j] += dp[i][j -coins[i]]
    print(dp[-1][m])