#11722 가장 긴 감소하는 부분 수열 
from sys import stdin 
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
dp = [1 for _ in range(n)]
maxima = 0
for i in range(1, n):            
    for j in range(i-1, -1, -1):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
    
print(max(dp))