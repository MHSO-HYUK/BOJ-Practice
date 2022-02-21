#2240 자두 나무
from sys import stdin
t, w = map(int, stdin.readline().split())
jd = [int(stdin.readline()) for _ in range(t)]
dp = [[0]*(w+1) for _ in range(t)]
p = w
if jd[0] == 2:
    dp[0] = [0, 1] + [0] * (w-1)
else:
    dp[0] = [1] + [0] * (w)
    
for i in range(1, t):
    if jd[i] == 1: #1번 나무
        dp[i][0] = dp[i-1][0] + 1
        for j in range(1, p+1, 2): # 2번
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) 
        for j in range(2, p+1, 2): # 1번 
            dp[i][j] = max(dp[i-1][j]+1, dp[i-1][j-1]+1)

            
    else: # 2번 나무
        dp[i][0] = dp[i-1][0]
        for j in range(1, p+1, 2): # 2번
            dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j] + 1) 
        for j in range(2, p+1, 2): # 2번
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) 

print(max(map(max, dp)))