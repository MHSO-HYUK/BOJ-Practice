# 1256 사전 
from sys import stdin 
import sys

n, m, k = map(int, stdin.readline().split())
# n개의 0 m개의 1로 이루어진 문자열에서 사전순으로 k번째 사전순
dp = [[1 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[n][m] < k:
    print(-1)
else:
    ans = ''
    while(1):
        if n ==0 or m == 0:
            ans += 'z'* m
            ans += 'a' * n
            break
        
        flag = dp[n-1][m]
        if k <= flag:
            ans += 'a'
            n -= 1
        else:
            ans += 'z'
            m -= 1
            k -= flag
    print(ans)