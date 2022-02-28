#2560 짚신벌레
# 태어난지 a일째 성체가 된다.
# 성체가 되고 매일 하나씩 개체를 만듬 
# 태어난지 b일이 되는 순간부터 새로운 개체를 만들지 않음 (일생동안 b- a의 개체를 만듬)
# 태어난지 d일 째 죽는다.
from sys import stdin 
a, b, d, n = map(int,stdin.readline().split())
dp = [0 for _ in range(n+2)]

for i in range(a):
    dp[i] = 1
    
for i in range(a, n+1):
    dp[i] = (dp[i-1] + dp[i-a]) % 1000
    
    if b <= i:
        dp[i] = (dp[i] - dp[i-b] + 1000) % 1000

ans = dp[n]
if n >= d: ans = (ans+1000-dp[n-d]) % 1000
print(ans)