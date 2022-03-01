# 2550 전구
from sys import stdin 

n = int(stdin.readline())
s = list(map(int, stdin.readline().split()))
f = list(map(int, stdin.readline().split()))
dp = [1 for _ in range(n)]
temp = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s[i] == f[j]:
            for k in range(i):
                if j > temp[k]:
                    dp[i] = max(dp[i], dp[k] + 1)
            temp[i] = j

print(max(dp))
i = dp.index(max(dp))
ans = [s[i]]
while(i != 0):
    for k in range(i-1, -1, -1):
        if dp[k] == dp[i] - 1 and temp[k] < temp[i]:
            ans.append(s[k])
            break
    i = k
ans.sort()
print(*ans)