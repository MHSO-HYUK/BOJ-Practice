# 2225 합분해 
n , k = map(int, input().split())
dp = [[0 for _ in range(n+2)] for _ in range(k+2)]
for i in range(n+2):
    dp[0][i] = 1
for i in range(k+2):
    dp[i][0] = 1

for i in range(1, k+2):
    for j in range(1, n+2):
        for p in range(j+1):
            dp[i][j] += dp[i-1][p]
        
print(dp[k-1][n] % 10**9)