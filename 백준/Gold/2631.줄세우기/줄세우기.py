#2631 줄세우기
from sys import stdin
import heapq
from copy import deepcopy

n = int(stdin.readline())
line = [0]
for _ in range(n):
    line.append(int(stdin.readline()))
dp = [0 for i in range(n+1)]
error = [[] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j: 
            if line[i] > line[j]:
                dp[line[i]] -= 1
                error[line[i]].append(line[j])
        if i > j:
            if line[i] < line[j]:
                dp[line[i]] -= 1
                error[line[i]].append(line[j])
                
temp = deepcopy(dp)
ans = 0
while(1):    
    flag = 0
    ans += 1
    heapq.heapify(dp)
    now = heapq.heappop(dp)
    idx = temp.index(now)
    temp[idx] = 0
    for i in range(len(temp)):
        if idx in error[i] and temp[i] < 0:
            temp[i] += 1
   
    for i in range(len(temp)):
        flag += temp[i]
    if flag == 0:
        break
    dp = deepcopy(temp)
print(ans)