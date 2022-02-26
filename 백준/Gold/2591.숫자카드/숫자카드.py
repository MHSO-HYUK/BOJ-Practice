#2591 숫자카드
# 1 ~ 34 카드 존재 
n = list(input().rstrip())
dp = [1 for _ in range(len(n))]
for i in range(len(n)-1):
    temp = 10*int(n[i]) + int(n[i+1])
    if int(n[i+1]) == 0:
        dp[i+1] = dp[i-1]
    elif 10<=temp<=34:
        dp[i+1] = dp[i] + dp[i-1]
    else:
        dp[i+1] = dp[i]
print(dp[-1])