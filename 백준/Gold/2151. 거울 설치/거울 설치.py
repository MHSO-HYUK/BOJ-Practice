# 2151 거울 설치
from sys import stdin 
import sys
sys.setrecursionlimit(10**5)
def dfs(x, y, cnt, d):
    global minima 
    a, b = x, y
    if cnt >= minima:
        return
    
    while(1):
        na, nb = a + dx[d], b + dy[d] 
        if 0 <= na <= n-1 and 0 <= nb <= n-1:
            if maps[na][nb] == '.': # 그냥 길인 경우 
                a, b = na, nb
                
            elif maps[na][nb] == '!': # 거울을 설치하는 경우
                if visit[na][nb][d-1] > cnt+1:
                    visit[na][nb][d-1] = cnt+1
                    dfs(na, nb, cnt+1, d-1 if d-1 >= 0 else 3) 
                if visit[na][nb][(d+1)%4] > cnt+1:
                    visit[na][nb][(d+1)%4] = cnt+1
                    dfs(na, nb, cnt+1, d+1 if d+1<4 else 0)
                a, b = na, nb # 그냥 뚫고 지나가는 경우

            elif maps[na][nb] == '*': # 벽을 만난 경우
                return

            elif [na, nb] == door[1]: # 나가는 문을 만난 경우
                minima = min(minima, cnt)
                return
            
            elif [na, nb] == door[0]: # 시작문을 만난 경우
                return # 잘못 온 것
        else:
            return
    
n = int(stdin.readline())
maps = list(list(stdin.readline().rstrip()) for _ in range(n))
door, mirror = [], []
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1) # 하 우 상 좌
minima = n**2

for i in range(n):
    for j in range(n):
        if maps[i][j] == '#':
            door.append([i, j])
d = []
for k in range(4):
    nx, ny = door[0][0] + dx[k] , door[0][1] + dy[k]
    if 0 <= nx <= n-1 and 0 <= ny <= n-1:            
        if maps[nx][ny] != '*':
            d.append(k) # 시작 방향 저장 
visit = [[[n**2, n**2, n**2, n**2] for _ in range(n)] for _ in range(n)]
for i in d:
    dfs(door[0][0], door[0][1], 0, i)
print(minima)