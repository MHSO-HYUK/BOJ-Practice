#2491 수열
from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
rev = nums[::-1]
dp, rp = [1 for _ in range(n)], [1 for _ in range(n)]
for i in range(n-1):
    if nums[i] <= nums[i+1]:
        dp[i+1] = dp[i] + 1
    else:
        dp[i+1] = 1
    if rev[i] <= rev[i+1]:
        rp[i+1] = rp[i] + 1
    else:
        rp[i+1] = 1
print(max(max(dp), max(rp)))