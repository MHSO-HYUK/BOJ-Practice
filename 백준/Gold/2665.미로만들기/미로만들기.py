from collections import deque
from sys import stdin
def miro(i, j, c):
    queue = deque([[i, j, c]])
    visit[i][j][c] = 1
    while(queue):
        x, y, c = queue.popleft()
        if(x == n-1 and y == n-1):
            return c
            break
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if(a<0 or b<0 or a>n-1 or b>n-1):
                continue
            if(maps[a][b] == 0 and visit[a][b][c+1] == 0): 
                visit[a][b][c+1] = 1
                queue.append([a,b,c+1])
            if(maps[a][b] == 1 and visit[a][b][c] ==0):
                visit[a][b][c] = 1
                queue.appendleft([a,b,c])

n = int(stdin.readline())
maps = []
visit = [[[0 for _ in range(n**2)]for _ in range(n)] for _ in range(n)]
for _ in range(n):
    maps.append(list(map(int, stdin.readline().rstrip())))
dx, dy = (1,-1, 0, 0), (0, 0, 1, -1)
print(miro(0, 0, 0)) # x, y, 뚫은 벽의 수