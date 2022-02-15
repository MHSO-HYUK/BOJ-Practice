#1699 제곱수의 합 
import math
n = int(input())
dp = [10**10 for _ in range(n+1)]
nums = [1]
dp[0], dp[1] =0, 1
for i in range(2, n+1):
    if not math.sqrt(i) % 1 : # 제곱수인 경우
        dp[i] = 1
        nums.append(i)
    else:
        for j in nums:
            dp[i] = min(dp[i], dp[i-j]+dp[j])
print(dp[n])