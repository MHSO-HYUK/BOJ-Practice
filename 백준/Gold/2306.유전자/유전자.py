t = input().strip()
dp = [[10**10 for _ in range(len(t))] for _ in range(len(t))]

def dfs(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    
    if dp[x][y] != 10**10:
        return dp[x][y]

    if (t[x] == 'a' and t[y] == 't') or (t[x] == 'g' and t[y] == 'c'):
        dp[x][y] = min(dp[x][y], dfs(x+1, y-1))
        
    for k in range(x, y):
        dp[x][y] = min(dp[x][y], dfs(x, k) + dfs(k+1, y))

    return dp[x][y]

print(len(t) - dfs(0, len(t)-1))