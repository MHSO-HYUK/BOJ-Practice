#7579 앱
from sys import stdin
n, m =map(int, stdin.readline().split()) #m바이트 이상을 확보하기 위한 앱 비활성화의 최소 비용
act, cost = [0] + list(map(int, stdin.readline().split())), [0] + list(map(int, stdin.readline().split()))
dp = [[0] *(sum(cost)+1) for _ in range(n+1)]
result = sum(cost)
for i in range(1, n+1):
    for j in range(1, sum(cost)+1):
            if j < cost[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(act[i] + dp[i-1][j-cost[i]], dp[i-1][j])
            
            if dp[i][j] >= m:
                result = min(result, j)
if m != 0:
    print(result)
else:
    print(m)