#4179 불!
from sys import stdin
from collections import deque
def fires():
    q = deque()
    fvisit = [[0]*m for _ in range(n)]
    while(fire):
        s, h = fire.pop()
        fvisit[s][h] = 1
        q.append([s, h])
    while(q):
        x, y= q.popleft()
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if 0<= a <=n-1 and 0<=b<=m-1:
                if maps[a][b] == '.' or maps[a][b] == 'J' :
                    if fvisit[a][b] == 0:
                        fvisit[a][b] = 1
                        maps[a][b] = 'F'
                        fire.append([a, b])
def move(s):
    queue = deque()
    queue.append([s[0], s[1], 0])
    visit = [[0]*m for _ in range(n)]
    visit[s[0]][s[1]] = 1
    while(queue):
        fires()
        for _ in range(len(queue)):
            x, y, cnt = queue.popleft()
            for k in range(4):
                a, b = x+dx[k], y+dy[k]
                if a<0 or a>n-1 or b<0 or b>m-1:
                    return cnt + 1
                if maps[a][b] == '.' and visit[a][b] == 0:
                    visit[a][b] = 1
                    queue.append([a, b, cnt+1])
                    
    return 'IMPOSSIBLE'

n, m = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(stdin.readline().rstrip()))
fire = []
for i in range(n):
    for j in range(m):
        if(maps[i][j] == 'J'):
            start = [i, j]
        if(maps[i][j] == 'F'):
            fire.append([i, j])
dx, dy= [1,-1,0,0], [0,0,1,-1]
print(move(start))