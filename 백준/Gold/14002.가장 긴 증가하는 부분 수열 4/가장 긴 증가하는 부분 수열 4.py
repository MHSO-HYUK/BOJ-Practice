#14002 가장 긴 증가하는 부분 수열
from sys import stdin
n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if num[i] > num[j] and dp[i] != dp[j] +1:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
maxidx = dp.index(max(dp))
cache = [[num[maxidx], max(dp)]]

for i in range(maxidx-1, -1, -1):
    if num[i] < cache[-1][0] and dp[i] == cache[-1][1] -1:
        cache.append([num[i], dp[i]])
for i in range(len(cache)-1, -1, -1):
    print(cache[i][0], end = ' ')