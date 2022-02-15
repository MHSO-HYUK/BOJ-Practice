# 11660 구간 합 구하기 5
from sys import stdin
n , m =map(int, stdin.readline().split())
maps =[]
quest = []
for _ in range(n):
    maps.append(list(map(int, stdin.readline().split())))
dp = [[0] *(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + maps[i][j]

for _ in range(m):
    a, b, c, d = map(int, stdin.readline().split())
    a, b, c, d = a-1, b-1, c-1, d-1
    
    central = dp[c+1][d+1]
    dc = dp[a][d+1] + dp[c+1][b] - dp[a][b]
    
    print(central - dc)