#16194 카드 구매하기 2
from sys import stdin
from copy import deepcopy

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
num.insert(0, 0)
dp = deepcopy(num)
for i in range(1, n+1):
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i-j] + dp[j])
print(dp[n])