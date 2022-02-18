#10942 펠린드롬?
from sys import stdin
n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
quest = []
for _ in range(m):
    quest.append(list(map(int, stdin.readline().split()))) # s / e 
    
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n- i):
        e = j + i
        if j == e:
            dp[j][e] = 1
            
        elif num[j] == num[e]:
            if j+1 == e : dp[j][e] = 1
            if dp[j+1][e-1] == 1 : dp[j][e] = 1
                
for a in quest:
    print(dp[a[0]-1][a[1]-1])