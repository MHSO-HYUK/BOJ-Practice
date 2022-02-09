#14502 연구소
from sys import stdin
from itertools import combinations
from collections import deque
def virus(virs):
    queue = deque()
    global cnt
    for i in range(len(virs)):
        queue.append(virs[i])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    while(queue):
        x, y = queue.popleft()
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if(0<=a<=n-1 and 0<=b<=m-1):
                if(maps[a][b] == 0 and visit[a][b] == 0):
                    cnt -= 1
                    visit[a][b] = 1
                    queue.append([a, b])
    return cnt  

n, m = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, stdin.readline().split())))
    
wall, vir = [], []
temp = 0
for i in range(n):
    for j in range(m):
        if(maps[i][j] == 0):
            wall.append([i, j])
            temp += 1
        if(maps[i][j] == 2):
            vir.append([i, j])
            
dx, dy = [1, -1, 0 , 0], [0, 0, 1, -1]
ans = 0
for w in combinations(wall, 3):
    cnt = temp - 3
    for i in w:
        maps[i[0]][i[1]] = 1
    ans = max(ans, virus(vir))
    for i in w:
        maps[i[0]][i[1]] = 0
print(ans)