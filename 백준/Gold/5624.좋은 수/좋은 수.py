# 5624 좋은 수
# 세개를 더했을 때 그 수가 되면 좋은 거
from sys import stdin

n= int(stdin.readline())
num = list(map(int, stdin.readline().split()))
dp = [0] * 400003
tmp = 200001
cnt = 0

for i in range(n):
    for j in range(i):
        if dp[num[i]  - num[j] + tmp] == 1:
            cnt += 1
            break
    for k in range(i+1):
        dp[num[i] + num[k] + tmp] = 1
        
print(cnt)