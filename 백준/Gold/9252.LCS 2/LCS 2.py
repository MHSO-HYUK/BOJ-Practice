#9252 LCS2
from sys import stdin
from copy import deepcopy

a, b = stdin.readline().rstrip(), stdin.readline().rstrip()
dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
ans = []
if dp[-1][-1] != 0:
    x, y = len(a), len(b)
    while(x>0 and y > 0):
        if dp[x][y-1] == dp[x][y]:
            y -= 1
        elif dp[x-1][y] == dp[x][y]:
            x -= 1
        else:
            ans.append(a[x-1])
            x -= 1
            y -= 1
    ans.reverse()
    print(''.join(ans))