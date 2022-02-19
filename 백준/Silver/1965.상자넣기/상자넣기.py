#1965 상자넣기
from sys import stdin

n = int(stdin.readline())
box = list(map(int, stdin.readline().split()))
dp =[1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))