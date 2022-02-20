# 2302 극장좌석
# 좌 우로는 옮길 수 있음 단 VIP는 못 옮김
from sys import stdin
n, m = int(stdin.readline()), int(stdin.readline())
maps = []
for _ in range(m):
    maps.append(int(stdin.readline()))
dp = [0 for _ in range(n+1)]
dp[0], dp[1] =1, 1
ans = []
if 1 in maps:
    temp = 0
else:
    temp = 1
for i in range(2, n+1):
    if i in maps:
        ans.append(temp)
        temp = 0
    elif i == n:
        temp += 1
        ans.append(temp)
    else:
        temp += 1
    dp[i] = dp[i-1] + dp[i-2]
    
sol = 1
for i in ans:
    sol *= dp[i]
print(sol)