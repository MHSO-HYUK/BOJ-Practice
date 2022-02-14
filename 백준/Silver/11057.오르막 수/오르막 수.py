#11057 오르막수 
def up(n):
    dp = [[0]*10 for _ in range(n+1)]
    for i in range(10):
        dp[0][i] = 1
    
    for i in range(1, n):
        for j in range(10):
            dp[i][j] = sum(dp[i-1][0:j+1])

    
    return sum(dp[n-1])%10007


n = int(input())
print(up(n))