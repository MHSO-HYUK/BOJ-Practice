def solution(s):
    answer = 1  
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    
    for i in range(len(s)):
        dp[i][i] = 1
    
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            dp[i+1][i] = 1
            answer = 2
    
    for i in range(3, len(s)+1):
        for j in range(len(s) - i+1):
            k = j + i - 1
            if s[j] == s[k] and dp[j+1][k-1]:
                dp[j][k] =1
                dp[k][j] = 1
                answer = max(answer, i)
    
    return answer