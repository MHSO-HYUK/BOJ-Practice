# 1949 우수마을
# 우수 마을 선정 인구수를 최대로 해야 한다.
# 우수 마을 끼리는 인접할 수 없다
# 선정되지 못한 마을은 적어도 하나의 우수마을과 인접해야 한다.
# 우수마을 주민 수의 총합을 출력한다.
from sys import stdin
import sys
sys.setrecursionlimit(10**5)
def usu(n):
    visit[n] = 1
    dp[n][0] = nums[n]
    for i in graph[n]:
        if not visit[i]:
            usu(i)
            dp[n][0] += dp[i][1]
            dp[n][1] += max(dp[i][0], dp[i][1])

p = int(stdin.readline())
nums = [0] + list(map(int, stdin.readline().split()))
graph = [[] for _ in range(p+1)]

for _ in range(p-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [0 for _ in range(p+1)]
dp = [[0, 0] for _ in range(p+1) ]
usu(1)
print(max(dp[1]))