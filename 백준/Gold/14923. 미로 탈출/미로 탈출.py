# 14923 미로탈출
from sys import stdin
from collections import deque
def miro():
    queue = deque()
    queue.append([hx, hy, 0, 0])
    visit = [[[0,0] for _ in range(m)] for _ in range(n)]
    visit[hx][hy][0] = 1
    while(queue):
        x, y, cnt, wall = queue.popleft()
        if x == ex and y == ey:
            return cnt
        if wall: # 이미 부심
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx <= n-1 and 0<= ny <= m-1:
                    if maps[nx][ny] == 0 and not visit[nx][ny][wall]:
                        visit[nx][ny][wall] = 1
                        queue.append([nx, ny, cnt+1, wall])
            
        else:
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx <= n-1 and 0<= ny <= m-1:
                    if maps[nx][ny] == 0 and not visit[nx][ny][wall]:
                        visit[nx][ny][wall] = 1
                        queue.append([nx, ny, cnt+1, wall])
                    if maps[nx][ny] == 1 and not visit[nx][ny][wall+1]:
                        visit[nx][ny][wall+1] = 1
                        queue.append([nx, ny, cnt+1, wall+1])
    return -1  

n, m = map(int, stdin.readline().split())
hx, hy = map(int, stdin.readline().split()) # 스타트
ex, ey = map(int, stdin.readline().split()) # 탈출 위치
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
hx, hy, ex, ey = hx-1, hy-1, ex-1, ey-1 
print(miro())