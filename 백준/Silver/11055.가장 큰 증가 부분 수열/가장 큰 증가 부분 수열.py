#11055 가장 큰 증가 부분 수열 
from sys import stdin
from copy import deepcopy
def maxima(nums):
    dp = deepcopy(nums)
    for i in range(n-1):
        temp = 0
        for j in range(i+1):
            if nums[j] < nums[i+1]: #이전 배열에서 오름 수열을 찾아 가장 큰 값을 더한다. 
                temp = max(temp, dp[j] + nums[i+1])

        if temp != 0:
            dp[i+1] = temp

        else:
            dp[i+1] = nums[i+1]    
    return max(dp)
    
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
print(maxima(nums))