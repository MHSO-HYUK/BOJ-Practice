#12852 1로 만들기 2
from collections import deque
n = int(input())
if n == 1:
    print(0)
    print(1)
else:
    INF = 10**10
    dp = [INF for _ in range(n+1)]
    dp[n] = 0
    queue = deque([n])
    while(queue):
        temp = queue.popleft()
        if not temp % 3:
            dp[temp//3] = min(dp[temp//3], dp[temp] + 1)
            if temp//3 == 1:
                break
            else:
                queue.append(temp//3)
        if not temp % 2:
            dp[temp//2] = min(dp[temp//2], dp[temp] + 1)
            if temp//2 == 1:
                break
            else:
                queue.append(temp//2)

        dp[temp-1] = min(dp[temp] + 1, dp[temp -1])
        if temp -1 == 1:
            break
        else:
            queue.append(temp-1)
    print(dp[1])
    ans = [1]
    for i in range(2, n+1):
        if dp[i] == dp[ans[-1]] - 1  and (i == 2* ans[-1] or i == 3* ans[-1] or i == ans[-1] + 1):
            ans.append(i)
    for i in range(len(ans)-1, -1, -1):
        print(ans[i], end = ' ')