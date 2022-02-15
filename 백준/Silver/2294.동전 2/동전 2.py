# 2294 동전 2
from sys import stdin

n, k = map(int, stdin.readline().split()) # k원이 되도록 
coin = []
for _ in range(n):
    coin.append(int(stdin.readline()))
    
dp = [-1 for _ in range(k+1)]
dp[0] = 0
for i in range(1, k+1):
    if i in coin:
        dp[i] = 1
    else:
        dp[i] = 10**10
        for j in range(1, i):
            if dp[i-j] != -1 and dp[j] != -1:
                dp[i] = min(dp[i-j] + dp[j], dp[i])
                
if dp[k] != 10**10 and dp[k] != -1:
    print(dp[k])
else:
    print(-1)