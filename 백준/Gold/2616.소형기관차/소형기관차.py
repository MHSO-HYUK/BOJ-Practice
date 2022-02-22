# 2616 소형기관차
from sys import stdin
n = int(stdin.readline()) # 기관차 갯수
s = list(map(int, stdin.readline().split())) # 객실 현황 
train = [0]
val = 0
for t in s:
    val += t
    train.append(val)
    
m = int(stdin.readline()) # 최대 끌 수 있는 갯수

dp = [[0]*(n+1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i*m, n+1):
        if i == 1:
            dp[i][j] = max(dp[i][j-1], train[j] - train[j-m])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-m] + train[j] - train[j-m])
print(dp[3][n])