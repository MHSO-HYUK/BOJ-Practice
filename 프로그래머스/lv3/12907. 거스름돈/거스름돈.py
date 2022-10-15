from copy import deepcopy
def solution(n, money):
    answer = 0
    dp = [[0 for _ in range(n+1)] for _ in range(len(money))]
    
    for m in range(len(money)):
        dp[m][0] = 1
        for i in range(1, n+1):
            dp[m][i] = dp[m-1][i]
            if i - money[m] >= 0:
                dp[m][i] += dp[m][i-money[m]]
        dp[m][i] = dp[m][i] % 1000000007
    return dp[-1][-1]