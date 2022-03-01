# 17144 미세먼지
from sys import stdin
import sys
from copy import deepcopy
sys.setrecursionlimit(10**5)
def clean():
    global cnt, maps
    un, clock = cleaner[0], cleaner[1]
    
    for i in range(un[0]-1, 0, -1):
        maps[i][un[1]] = maps[i-1][un[1]]
        
    for i in range(un[1], m-1):
        maps[0][i] = maps[0][i+1]
        
    for i in range(un[0]):
        maps[i][m-1] = maps[i+1][m-1]
        
    for i in range(m-1, un[1], -1):
        maps[un[0]][i] = maps[un[0]][i-1]
        

    for i in range(clock[0]+1, n-1):
        maps[i][clock[1]] = maps[i+1][clock[1]]
        
    for i in range(clock[1], m-1):
        maps[n-1][i] = maps[n-1][i+1]
        
    for i in range(n-1, clock[0], -1):
        maps[i][m-1] = maps[i-1][m-1]
        
    for i in range(m-1, clock[1], -1):
        maps[clock[0]][i] = maps[clock[0]][i-1]
        
    maps[un[0]][un[1]] = -1
    maps[clock[0]][clock[1]] = -1
    maps[un[0]][un[1]+1] = 0
    maps[clock[0]][clock[1]+1] = 0

    cnt += 1
    if cnt == t:
        ans = 0
        for i in range(n):
            ans += sum(maps[i])
        print(ans+2)
        sys.exit()
    else:
        spread()
        
        
def spread():
    global maps
    temp = [[0 for _ in range(m)] for _ in range(n)]
    dust = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0 and maps[i][j] != -1:
                temp[i][j] = maps[i][j]
                dust.append([i, j])
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for k in dust:
        for i in range(4):
            x, y = k[0] + dx[i], k[1] +dy[i]
            if 0<=x<=n-1 and 0<=y<=m-1:
                if maps[x][y] != -1:
                    temp[x][y] += maps[k[0]][k[1]] // 5
                    temp[k[0]][k[1]] -= maps[k[0]][k[1]] // 5
    
    maps = deepcopy(temp)
    clean()

    
n, m, t = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, stdin.readline().split())))
cleaner = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == -1:
            cleaner.append([i, j])
cnt = 0
spread()