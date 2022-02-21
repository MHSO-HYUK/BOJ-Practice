#2502 떡 먹는 호랑이 
import sys
a, b = map(int, input().split())
dp = [0 for _ in range(a)]
dp[a-1] = b

for i in range(1, b+1):
    for j in range(i+1, b+1):
        dp[0], dp[1] = i, j
        for k in range(2, a-1):
            dp[k] = dp[k-1] + dp[k-2]
        if dp[a-1] == dp[a-2] + dp[a-3]:
            print(i)
            print(j)
            sys.exit()