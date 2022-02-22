#11066 파일 합치기
from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    book = list(map(int, stdin.readline().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # 기본 비용을 반영하는 과정 
    for i in range(n-1):
        dp[i][i+1] = book[i] + book[i+1]
        for j in range(i+2, n):
            dp[i][j] = dp[i][j-1] + book[j]
    
    # 추가 비용을 반영하는 과정 
    for d in range(2, n):
        for i in range(n-d):
            j = i + d
            minima = [dp[i][p] + dp[p+1][j] for p in range(i, j)]
            dp[i][j] += min(minima)
    print(dp[0][n-1])
