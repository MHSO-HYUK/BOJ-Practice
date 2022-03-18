# 16973 직사각형 탈출 
from sys import stdin 
from collections import deque
def bfs():
    global sx, sy, fx, fy
    visit = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque([[sx, sy, 0, [sx, sx+h-1, sy, sy+w-1]]]) # 위 아래 좌 우
    visit[sx][sy] = 1
    while(queue):
        x, y, cnt, sq = queue.popleft()
        if [x, y] == [fx, fy]:
                return cnt
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]            
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if not visit[nx][ny]:
                    flag = True
                    visit[nx][ny] = 1
                    ax, bx, ay, by = sq[0]+dx[k], sq[1] + dx[k], sq[2] + dy[k], sq[3] + dy[k]
                    if not (0 <= ax <= n-1 and 0 <=bx <=n-1 and 0 <= ay <= m-1 and 0 <= by <= m-1):
                        flag = False
                    if flag:
                        for i in range(ax, bx+1):
                            if maps[i][ay]:
                                flag = False
                                break
                    if flag:
                        for i in range(ax, bx+1):
                            if maps[i][by]:
                                flag = False
                                break
                    if flag:
                        for j in range(ay, by+1):
                            if maps[ax][j]:
                                flag = False
                                break
                    if flag:
                        for j in range(ay, by+1):
                            if maps[bx][j]:
                                flag = False
                                break
                    if flag:
                        queue.append([nx, ny, cnt+1, [sq[0]+dx[k], sq[1] + dx[k], sq[2] + dy[k], sq[3] + dy[k]]])
    return -1

n, m = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
h, w, sx, sy, fx, fy = map(int, stdin.readline().split())
sx, sy, fx, fy = sx-1, sy-1, fx-1, fy-1
sq =[]
dx, dy= (1, -1, 0, 0), (0, 0, 1, -1)
for i in range(sx, sx+h):
    for j in range(sy, sy+w):
        if i == sx or i == sx+h-1 or j == sy or j ==sy+w-1:
            sq.append([i, j])

print(bfs())