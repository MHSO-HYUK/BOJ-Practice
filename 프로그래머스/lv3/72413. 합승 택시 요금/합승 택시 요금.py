def solution(n, s, a, b, fares):

    dp = [[1e9 for _ in range(n+1)] for _ in range(n+1)]
    for x, y, z in fares:
        dp[x][y] = z
        dp[y][x] = z
    
    for i in range(1, n+1):
        dp[i][i] = 0
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if i != k and j != k and i != j:
                    dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])

    
    # (s에서 시작 -> 특정 지점) + (특정 지점 -> A) + (특정 지점 -> B) 의 최소값
    minima = 1e9
    for i in range(1, n+1): # 특정 지점 
        minima = min(minima, dp[s][i] + dp[i][a] + dp[i][b])
        
    return minima