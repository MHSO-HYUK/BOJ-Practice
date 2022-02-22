#1958 LCS 3 
from sys import stdin
import sys
a, b, c = list(stdin.readline().rstrip()), list(stdin.readline().rstrip()), list(stdin.readline().rstrip())
dp = [[[0 for _ in range(len(c)+1)] for _ in range(len(b)+1)] for _ in range(len(a)+1)]
A, B, C=len(a), len(b), len(c)
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        for k in range(1, len(c)+1):
            if a[i-1] == b[j-1] == c[k-1]:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k-1] + 1)
                
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
print(dp[A][B][C])