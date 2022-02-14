#11052 카드 구매하기 
from sys import stdin 
from collections import deque
def card(n):
    dp = [0 for _ in range(n+1)]
    for k in range(1, n+1):
        dp[k] = price[k-1]
        
    for i in range(2, n+1):
        for j in range(1, i//2 +1):
            if dp[j] + dp[i - j] > dp[i]:
                dp[i] = dp[j] + dp[i-j]

            else:
                continue

    return dp[n]

n = int(stdin.readline())
price = list(map(int, stdin.readline().split())) # idx+1개의 카드가 들어있음->n개 사는데 필요한 최댓값
print(card(n))