#2482 색상환
#인접한 두 색은 선택불가!
from sys import stdin
n, k = int(stdin.readline()), int(stdin.readline()) #n개의 색상환에서 k개를 고르는 가짓수
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
#1. 1번을 고르는 경우
for j in range(1, k+1):
    for i in range(2, n+1):
        if j == 1:
            dp[i][j] = i
        else:
            if i-2 >=0:
                dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) %1000000003

print(dp[n][k])