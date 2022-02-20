#5582 공통 부분 문자열 
from sys import stdin
a, b = list(stdin.readline().rstrip()), list(stdin.readline().rstrip())
p, q = len(a), len(b)
dp =[[0]*(q+1) for _ in range(p+1)]
for i in range(1, p+1):
    for j in range(1, q+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = 0
print(max(map(max, dp)))