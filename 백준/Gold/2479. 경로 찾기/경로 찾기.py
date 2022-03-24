# 2479 경로찾기
from sys import stdin
import sys
from collections import defaultdict
def dfs(now, road):
    if now == e:
        print(*road)
        sys.exit()
    
    for i in range(k):
        temp = list(ham[now])
        temp[i] = str(abs(1- int(temp[i])))
        temp = ''.join(temp)
        if temp in ham and ham[temp][0] == 0:
            ham[temp][0] = 1
            dfs(ham[temp][1], road + [ham[temp][1]])
            ham[temp][0] = 0

n, k = map(int, stdin.readline().split())
ham = defaultdict(list)
for i in range(n):
    ham[i+1] = ''.join(list(stdin.readline().rstrip()))
    ham[ham[i+1]] = [0, i+1]
s, e = map(int, stdin.readline().split())
dfs(s, [s])
print(-1)