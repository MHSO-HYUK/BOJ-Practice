n, k = map(int, input().split())
dp = [0 for _ in range(n+1)]
dp[0] = 1
if k > n // 2:
    k = n-k

for i in range(1, n//2+1):
    dp[i] = dp[i-1] * (n-i+1) // (i)
    if i == k:
        break
        
    
if n % 2:
    dp[n : n//2: -1] = dp[0: n//2+1]
else: # 짝수
    dp[n : n//2 : -1] = dp[0: n//2]
    
print(dp[k]%10007)