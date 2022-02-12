#1726 로봇
from sys import stdin
from collections import deque
def robot(s, f):
    queue = deque()
    queue.append([s[0]-1, s[1]-1, s[2]-1, 0])
    visit = [[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]
    visit[s[0]-1][s[1]-1][s[2]-1] = 1
    while(queue):
        x, y, loc, cnt  = queue.popleft()
        if([x, y, loc] == [f[0]-1, f[1]-1, f[2]-1]):
            return cnt
        
        for k in range(1, 4):
            a, b = x + (k*dx[loc]) , y + (k*dy[loc])
            if 0<=a<=n-1 and 0<=b<=m-1:
                if maps[a][b] == 1:
                    break
                if maps[a][b] == 0 and visit[a][b][loc] == 0:
                    visit[a][b][loc] = 1
                    queue.append([a, b, loc, cnt+1]) 
                    
        if loc == 0 or loc == 1:
            if(visit[x][y][2] == 0):
                visit[x][y][2] = 1
                queue.append([x, y, 2, cnt+1])
                
            if(visit[x][y][3] == 0):
                visit[x][y][3] = 1
                queue.append([x, y, 3, cnt+1])
                
        elif loc == 2 or loc == 3:
            if(visit[x][y][0]== 0):
                visit[x][y][0] = 1
                queue.append([x, y, 0, cnt+1])
                
            if(visit[x][y][1] == 0):
                visit[x][y][1] = 1
                queue.append([x, y, 1, cnt+1])

n, m = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, stdin.readline().split())))

start = list(map (int, stdin.readline().split()))
finish = list(map (int, stdin.readline().split()))
dx, dy = [0, 0, 1 ,-1], [1, -1, 0, 0] # 동 서 남 북  
print(robot(start, finish))