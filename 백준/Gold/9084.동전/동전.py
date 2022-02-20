#9084 동전
from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    coin = list(map(int, stdin.readline().split()))
    k = int(stdin.readline())
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    for i in coin:
        for j in range(1, k+1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    print(dp[k])