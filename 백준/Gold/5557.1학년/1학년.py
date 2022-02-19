#5557 1학년
from itertools import product
from sys import stdin    
n = int(input())
s = list(map(int, input().split()))
dp = [[0] * 21 for i in range(n)]
dp[0][s[0]] = 1
for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if 0 <= j + s[i] <= 20: 
                dp[i][j + s[i]] += dp[i - 1][j]
                
            if 0 <= j - s[i] <= 20: 
                dp[i][j - s[i]] += dp[i - 1][j]
                
print(dp[n - 2][s[n-1]])