#2133 타일 채우기

n = int(input())
dp = [0 for _ in range(31)] # 2 / 4

dp[2] = 3
temp = 0
for i in range(4, n+2, 2):
    dp[i] = 3 * dp[i-2] + temp + 2
    temp += 2*dp[i-2]


print(dp[n])