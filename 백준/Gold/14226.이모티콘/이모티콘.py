#14226 이모티콘
#현재 1개 -> 복사 / 붙여넣기 / 하나삭제 중 하나 가능(1초)
from collections import deque
s = int(input())
dp = [[-1] * (s+1) for _ in range(s+1)]
queue = deque([[1, 0]])
while(queue):
    n, c = queue.popleft()
    if(n == s):
        print(dp[n][c])
        break
    dx = [c, 0, -1]
    for i in range(3):
        nx = n + dx[i]
        if(nx<0 or nx> s):
            continue
        if(dp[nx][n] == -1 and i == 1):
            dp[nx][n] = dp[n][c] + 1
            queue.append([nx, n])
            
        if(dp[nx][c] == -1 and i != 1):
            dp[nx][c] = dp[n][c] + 1
            queue.append([nx, c])