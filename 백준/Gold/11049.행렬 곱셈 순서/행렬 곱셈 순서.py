#11049 행렬 곱셈 순서
from sys import stdin
num = int(stdin.readline())
mats = []
for _ in range(num):
    mats.append(list(map(int, stdin.readline().split())))

dp = [[0 for _ in range(num)] for _ in range(num)]

for i in range(1, num):
    for j in range(num - i):
        dp[j][j+i] = 10**10
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + mats[j][0] * mats[k][1] * mats[j+i][1])
        
print(dp[0][num-1])
















