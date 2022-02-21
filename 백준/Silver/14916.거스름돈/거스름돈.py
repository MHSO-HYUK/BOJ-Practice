#14916 거스름돈
n = int(input())
dp = [10**10 for _ in range(n+5)]
dp[2], dp[5] = 1, 1
for i in range(1, n+1):
    for j in range(1, i//2+1):
        dp[i] = min(dp[i], dp[i-j] +dp[j])
if dp[n] == 10**10:
    print(-1)
else:
    print(dp[n])