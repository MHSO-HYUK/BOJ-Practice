# 13398 연속합 2
from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
dp = [[0, 0, 0] for _ in range(n)] #제거하지 않았을 때 값 / 제거했을 때 최댓값
if n == 1:
    print(nums[0])
else:
    dp[0] = [max(nums[0], 0), 0, 0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0] + nums[i], 0) # 제거하지 않았을 때 최대값
        dp[i][1] = max(dp[i-1][0], 0) # i를 제거했을 때 값
        dp[i][2] = max(max(dp[i-1]) + nums[i], 0) #제거된 이후의 최대값
    ans = max(map(max, dp))
    if ans != 0:
        print(ans)
    else:
        print(max(nums))