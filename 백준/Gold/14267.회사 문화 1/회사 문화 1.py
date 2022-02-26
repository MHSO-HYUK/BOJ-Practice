# 14267 회사문화
from sys import stdin
import sys
sys.setrecursionlimit(10**5)
def phrase(n):
    dp[n] += dp[sup[n]]
    if imp[n]:
        for i in range(len(imp[n])):
            phrase(imp[n][i])

n, m = map(int, stdin.readline().split())
level = list(map(int, stdin.readline().split()))
sup, imp = [0 for _ in range(n+1)], [[] for _ in range(n+1)]
for i in range(1, n):
    imp[level[i]].append(i+1)
    sup[i+1] = level[i]
    
dp = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    dp[a] += b

phrase(1)
for i in range(1, n+1):
    print(dp[i], end = ' ')