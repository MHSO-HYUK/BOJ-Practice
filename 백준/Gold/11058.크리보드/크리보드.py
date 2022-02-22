# 11058 크리포드
from collections import deque
n = int(input())
# 버퍼에 있는 갯수 + 횟수 -> 3차원 
dp = [[0, 0] for _ in range(n+2)]

maxima = 0
queue = deque()
queue.append([0, 0, 0])
while(queue):
    p, b, num = queue.popleft()
    if num >= n:
        if num == n:
            maxima = max(maxima, p)
    else:
        if not (dp[num+1][0] >= p+1 and dp[num+1][1] >= b):
            dp[num+1] = [p+1, b]
            queue.append([p+1, b, num+1])
            
        if not (dp[num+2][0] >= p and dp[num+2][1] >= p):
            dp[num+2] = [p, p]
            queue.append([p, p, num+2])
            
        if not (dp[num+1][0] >= p+b and dp[num+1][1] >= b):
            dp[num+1] = [p+b, b]
            queue.append([p+b, b, num+1])
            
            
print(maxima)