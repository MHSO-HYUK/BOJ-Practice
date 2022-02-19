#15988 1, 2, 3 더하기 3
from sys import stdin
t = int(stdin.readline())
q = []
for _ in range(t):
    q.append(int(stdin.readline()))
search = max(q)

dp = [0 for _ in range(search+1)]
dp[1], dp[2], dp[3], dp[4] = 1, 2, 4, 7
for i in range(5, search+1):
    dp[i] = (dp[i-1] * 2 - dp[i-4]) % 1000000009

for i in q:
    print(dp[i] )