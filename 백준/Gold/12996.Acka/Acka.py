# 12996 ACKA
from sys import stdin 
def acka(n, a, b, c):
    if n == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0
        
    elif a<0 or b<0 or c<0:
        return 0
    elif dp[n][a][b][c] != -1:
        return dp[n][a][b][c]
    else:
        dp[n][a][b][c] = 0
        
        dp[n][a][b][c] += acka(n-1, a-1, b-1, c-1)
        dp[n][a][b][c] %= 1000000007
        dp[n][a][b][c] += acka(n-1, a-1, b-1, c)
        dp[n][a][b][c] %= 1000000007
        dp[n][a][b][c] += acka(n-1, a-1, b, c)
        dp[n][a][b][c] %= 1000000007
        dp[n][a][b][c] += acka(n-1, a-1, b, c-1)
        dp[n][a][b][c] %= 1000000007
        dp[n][a][b][c] += acka(n-1, a, b-1, c-1)
        dp[n][a][b][c] %= 1000000007
        dp[n][a][b][c] += acka(n-1, a, b, c-1)
        dp[n][a][b][c] %= 1000000007
        dp[n][a][b][c] += acka(n-1, a, b-1, c)
        dp[n][a][b][c] %= 1000000007
        return dp[n][a][b][c] % 1000000007
    
s, *song = map(int, stdin.readline().split())
if sum(song) < s:
    print(0)
else:

    dp = [[[[-1 for _ in range(song[2]+1)] for _ in range(song[1]+1)] for _ in range(song[0]+1)] for _ in range(s+1)]
    print(acka(s, song[0], song[1], song[2]))