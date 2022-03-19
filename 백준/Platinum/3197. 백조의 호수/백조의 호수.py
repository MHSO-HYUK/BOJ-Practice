# 3197 백조의 호수
# 물 공간과 접촉한 빙판은 녹음 
from sys import stdin
from collections import deque
from copy import deepcopy
def crash():
    while ice:
        x, y = ice.popleft()
        if maps[x][y] == 'X':
            maps[x][y] = '.'
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if not cvisit[nx][ny]:
                    cvisit[nx][ny] = 1
                    if maps[nx][ny] == 'X':
                        icetemp.append([nx, ny])
                    else:
                        ice.append([nx, ny])
                    
    
def meet():
    while(queue):
        x, y = queue.popleft()
        if [x, y] == swan[1]:
            return True
        
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx <= n-1 and 0<= ny <= m-1:
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    if maps[nx][ny] == '.':   
                        queue.append([nx, ny])
                    else:
                        queuetemp.append([nx, ny])
    return False

n, m = map(int, stdin.readline().split())
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
swan, maps = [], []
cvisit =  [[0 for _ in range(m)] for _ in range(n)]
visit =  [[0 for _ in range(m)] for _ in range(n)]
ice, icetemp, = deque(), deque()
queue, queuetemp = deque(), deque()

for i in range(n):
    t = list(stdin.readline().rstrip())
    for j in range(m):
        if t[j] == 'L':
            t[j] = '.' 
            swan.append([i, j])
            ice.append([i, j])
        elif t[j] == '.':
            cvisit[i][j] = 1
            ice.append([i, j])
    maps.append(t)
queue.append([swan[0][0], swan[0][1]])
day = 0
while(1):
    crash()
    if meet():
        break
    queue, ice = queuetemp, icetemp
    queuetemp, icetemp = deque(), deque()
    day += 1
print(day)