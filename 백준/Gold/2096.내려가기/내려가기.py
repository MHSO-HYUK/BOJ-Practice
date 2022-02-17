#2096 내려가기
from sys import stdin
from copy import deepcopy

n = int(stdin.readline())
dp = [0 for _ in range(3)]
dp2 =  [0 for _ in range(3)]
for _ in range(n):
    maps = list(map(int, stdin.readline().split()))
    temp = deepcopy(dp)
    temp2 = deepcopy(dp2)
    for i in range(3):
        dp[i] = maps[i]
        dp2[i] = maps[i]
        if i == 0:
            dp[i] += max(temp[0], temp[1])
            dp2[i] += min(temp2[0], temp2[1])
        if i == 1:
            dp[i] += max(temp)
            dp2[i] += min(temp2)
        if i == 2:
            dp[i] += max(temp[1], temp[2])
            dp2[i] += min(temp2[1], temp2[2])
    
print(max(dp), min(dp2))