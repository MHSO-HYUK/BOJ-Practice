# 1563 개근상
# 지각 두번 이상 // 결석 3연속 시 못 받음


from sys import stdin
n = int(stdin.readline())
dp = [[[0,0,0] for _ in range(2)] for _ in range(n+3)]
dp[1][0][0] = dp[1][1][0] = dp[1][0][1] = 1
for i in range(2, n+1):
    dp[i][0][0] = sum(dp[i-1][0]) % 1000000
    dp[i][1][0] = (sum(dp[i-1][0]) + sum(dp[i-1][1])) % 1000000
    dp[i][0][1] = dp[i-1][0][0] % 1000000
    dp[i][1][1] = dp[i-1][1][0] % 1000000
    dp[i][0][2] = dp[i-1][0][1] % 1000000
    dp[i][1][2] = dp[i-1][1][1] % 1000000

print((sum(dp[n][0]) + sum(dp[n][1]))% 1000000)
