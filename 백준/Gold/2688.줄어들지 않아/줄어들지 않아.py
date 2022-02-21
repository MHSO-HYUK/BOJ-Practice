#2688 줄어들지 않아
t = int(input())
q= []
for _ in range(t):
    q.append(int(input()))
flag = max(q)
dp = [[0]*10 for _ in range(flag+1)]
dp[1] = [1]*10
for i in range(2, flag+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][k] += dp[i-1][j]

    
for v in q:
    print(sum(dp[v]))