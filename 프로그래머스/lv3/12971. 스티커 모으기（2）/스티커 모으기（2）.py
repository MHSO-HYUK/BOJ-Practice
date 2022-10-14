def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker[0]
    if 2 <= len(sticker) <= 3:
        return max(sticker)
    
    dp = [0 for _ in range(len(sticker))]
    dp[0] = sticker[0]
    for i in range(1, len(sticker)-1):
        for j in range(i-2, i-4, -1):
            dp[i] = max(dp[i], dp[j] + sticker[i])
    
    answer = max(dp)
    
    dp = [0 for _ in range(len(sticker))]
    for i in range(1, len(sticker)):
        for j in range(i-2, i-4, -1):
            dp[i] = max(dp[i], dp[j] + sticker[i])
            
    answer = max(answer, max(dp))
    return answer