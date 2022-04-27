# 20058 마법사 상어와 파이어스톰
from sys import stdin 
from collections import deque
def separate(new_maps, l):
    ret_maps = [[0 for _ in range(2**n)] for _ in range(2**n)]
    sx, sy = 0, 0
    while(1):
        cache = []
        for i in range(sx, sx+2**l):
            temp = []
            for j in range(sy, sy+2**l):
                temp.append(new_maps[i][j])
            cache.append(temp)
        
        for y in range(2**l):
            cnt = 0
            for x in range(2**l-1, -1, -1):
                ret_maps[sx+y][sy+cnt] = cache[x][y]
                cnt += 1
        
        sy = sy + 2**l
        if sy == 2**n:
            sx += 2**l
            sy = 0
            if sx == 2**n:
                break
    
    return ret_maps

def bfs(x, y):
    queue = deque([[x, y]])
    visit[x][y] = 1
    cnt = 0
    while(queue):
        x, y = queue.popleft()
        cnt += 1
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx <= 2**n-1 and 0 <= ny <= 2**n-1:
                if not visit[nx][ny] and maps[nx][ny]:
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
    return cnt
n, q = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(2**n))
comm = deque(map(int, stdin.readline().split()))
dx, dy= [1, -1, 0, 0], [0, 0, 1, -1]
while(comm):
    l = comm.popleft()
    maps = separate(maps, l)
    melt = [[0 for _ in range(2**n)] for _ in range(2**n)]
    for i in range(2**n):
        for j in range(2**n):
            if maps[i][j]:
                cnt = 0
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0 <= nx <= 2**n-1 and 0 <= ny <= 2**n-1:
                        if maps[nx][ny]:
                            cnt += 1
                if cnt < 3:
                    melt[i][j] += 1
                    
    for i in range(2**n):
        for j in range(2**n):
            maps[i][j] -= melt[i][j]

print(sum(map(sum, maps))) 
visit = [[0 for _ in range(2**n)] for _ in range(2**n)]
maxima = 0
for i in range(2**n):
    for j in range(2**n):
        if not visit[i][j] and maps[i][j]:
            maxima = max(maxima, bfs(i, j))
print(maxima)