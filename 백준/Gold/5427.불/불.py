#5427 불
# 불이 붙으려는 칸 + 이미 붙은 칸은 이동 불가하다! 
from sys import stdin
from collections import deque
def fire():
    q = deque()
    while(fires):    
        q.append(fires.pop())
    while(q):
        x, y = q.popleft()
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if(0<=a<=n-1 and 0<=b<=m-1):
                if(maps[a][b] == '.'):
                    maps[a][b] = '*'
                    fires.append([a, b])
                    
def move(sx, sy):
    visit = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque([[sx, sy, 0]])
    visit[sx][sy] = 1
    while(queue):
        fire()
        for _ in range(len(queue)):
            x, y, cnt = queue.popleft()
            for k in range(4):
                a, b= x+dx[k], y+dy[k]
                if a<0 or a>n-1 or b<0 or b>m-1:
                    return cnt + 1
                
                if maps[a][b] == '.' and visit[a][b] == 0:
                    visit[a][b] = 1
                    queue.append([a, b, cnt+1])
                    
    return 'IMPOSSIBLE'          
    
t = int(stdin.readline())
dx, dy = [1,-1,0,0], [0,0,1,-1]
for _ in range(t):
    m,n = map(int, stdin.readline().split())
    maps, fires = [], []
    for _ in range(n):
        maps.append(list(stdin.readline().rstrip()))
    for i in range(n):
        for j in range(m):
            if(maps[i][j] == '@'):
                sx, sy = i, j
            if(maps[i][j] == '*'):
                fires.append([i,j])

    print(move(sx, sy))