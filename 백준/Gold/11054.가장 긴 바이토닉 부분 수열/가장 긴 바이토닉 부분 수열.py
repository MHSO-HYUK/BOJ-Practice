from sys import stdin
n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
rev = num[::-1]
dp =[1 for _ in range(n)]
dp2 =[1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j]+1)
        if rev[i] > rev[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

ans = []
for i in range(n):
    ans.append(dp[i] + dp2[n-i-1])
print(max(ans) - 1)
