# 2565 전깃줄 
from sys import stdin
n = int(stdin.readline())
con = []
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    con.append([a, b])
con.sort()
rev = con[::-1]
up = [1 for _ in range(n+1)]
down = [1 for _ in range(n+1)]
for i in range(n):
    for j in range(i):
        if con[i][0] > con[j][0] and con[i][1] > con[j][1]:
            up[i] = max(up[i] , up[j] + 1)
        if rev[i][0] > rev[j][0] and rev[i][1] > rev[j][1]:
            down[i] = max(down[i], down[j] + 1)
maxima = max(max(up), max(down))
print(n - maxima)