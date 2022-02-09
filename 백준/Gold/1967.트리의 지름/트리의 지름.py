#1967 트리의 지름
from sys import stdin 
import sys
sys.setrecursionlimit(10**4)
def tree(i):
    if(not graph[i]):
        dp[i] = [[0], cost[i]]
        return dp[i]
    else:
        maxima, temp = 0, []
        for v in graph[i]:
            t = tree(v)
            temp.append(t[1])
            temp.sort()
        if(len(temp) >= 2):
            dp[i][0].append(temp[-1]) # 자식의 최대 가중치 
            dp[i][0].append(temp[-2]) # 자식의 최대 가중치  
        else:
            dp[i][0].append(temp[0])
        dp[i][1] = max(dp[i][0]) + cost[i]
        
        return dp[i]
        
n = int(stdin.readline())
graph = [[] for _ in range(n+1)]
cost = [0 for _ in range(n+1)]
line = []
for _ in range(n-1):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append(b)
    cost[b] = c
dp = [[[], []] for _ in range(n+1)] # 가중치 // 최대 가중치 
tree(1)
maxima = 0
for i in range(1, n+1):
    maxima = max(maxima, sum(dp[i][0]))
print(maxima)