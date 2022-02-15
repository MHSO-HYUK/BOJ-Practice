#12865 평범한 배낭 
from sys import stdin
n, k = map(int, stdin.readline().split()) # k: 최대로 넣을 수 있는 무게 
bag = [[0, 0]]

for _ in range(n):
    w, v = map(int ,stdin.readline().split())
    bag.append([w, v])
    
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = bag[i][0]
        v = bag[i][1]
        
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])
        
print(dp[n][k])