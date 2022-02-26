#2643 색종이 올려놓기 
# 맨위 색종이보다 작아야함
# 맨위의 색종이의 변은 평행해야 한다. 
from sys import stdin
n = int(stdin.readline())
paper = list(sorted(list(map(int,stdin.readline().split()))) for _ in range(n))
paper.sort()
dp = [1 for _ in range(n)]
for i in range(1, n):
    for v in range(i):
        if paper[v][1] <= paper[i][1]:
            dp[i]= max(dp[i], dp[v] + 1)
        
        if paper[v][0] <= paper[i][1] and paper[v][1] <= paper[i][0]:
            dp[i]= max(dp[i], dp[v] + 1)
            
        if paper[v][0] >= paper[i][1] and paper[v][1] >= paper[i][0]:
            dp[i]= max(dp[i], dp[v] + 1)

print(max(dp))