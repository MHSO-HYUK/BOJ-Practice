# 11967 불켜기
# 불이 켜진 방에만 들어갈 수 있음 
from sys import stdin
import sys
sys.setrecursionlimit(10**5)
def dfs(x, y):
    global maxima, visit
    log[x][y] = 1
    for k in info[x][y]:
        light[k[0]][k[1]] += 1
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if light[i][j]:
                cnt += 1
    maxima = max(maxima, cnt)
    
    
    for k in range(4): # 새로 들어온 방에서 뻗을 수 있는가?
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<=n-1 and 0<=ny <=n-1:
            if not log[nx][ny]: # 아직 안들어감
                target[nx][ny] = 1
    
    for i in range(n): # 이전에 못갔던 방으로 갈 수 있는가?
        for j in range(n):
            if target[i][j] and light[i][j]: # 안들어갔는데 불 켜짐
                target[i][j] = 0
                dfs(i, j)
                
n, m =map(int,stdin.readline().split())
info = [[[] for _ in range(n)] for _ in range(n)]
dx, dy= [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(m):
    x, y, a, b = map(int, stdin.readline().split())
    info[x-1][y-1].append([a-1, b-1])
light, target = [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]
light[0][0] = 1
maxima = 0
log =[[0]*n for _ in range(n)]
log[0][0] = 1
dfs(0, 0)
print(maxima)