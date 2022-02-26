# 2637 장난감 조립 
from sys import stdin
def toy(k):
    if visit[k] == 1:
        return k
    elif len(graph[k]) == 0:
        dp[k][k] = 1
        visit[k] = 1
        return k
    else:
        for v in graph[k]:
            idx = toy(v[0])
            for i in range(n+1):
                dp[k][i] += v[1] * dp[idx][i]
        visit[k] = 1
        return k

n, m = int(stdin.readline()), int(stdin.readline())
graph = [[] for _ in range(n+1)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, stdin.readline().split())
    graph[x].append([y,z])
visit = [0 for _ in range(n+1)]
toy(n)
for i in range(1, n+1):
    if dp[n][i]:
        print(i, dp[n][i])