#10844 쉬운 계단수 
#각 자릿수의 차이가 1나는 수
from sys import stdin
n = int(stdin.readline())
dp = [[0] * 10 for _ in range(101)]
for i in range(1, 10):
    dp[0][i] = 1
for i in range(1, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
            
        else: dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            
print(sum(dp[n-1])%1000000000)