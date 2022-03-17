# 6087 레이저 통신
from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(10**5)
def bfs(x, y):
    global minima
    queue = deque([[x, y, -10 ,0]])
    while(queue):
        x, y, before, cnt = queue.popleft()
        if [x, y] == room[1]:
            minima = min(minima, cnt)
        else:
            for k in range(4):
                nx, ny = x+ dx[k], y + dy[k]
                if 0<=nx<=n-1 and 0<=ny<=m-1:
                    if maps[nx][ny] == '.' or maps[nx][ny] == 'C':
                        if k != before and abs(k-before) != 2: # 90도 트는 경우
                            if visit[nx][ny][k] > cnt+1:
                                visit[nx][ny][k] = cnt+1
                                queue.append([nx, ny, k, cnt+1])
                        elif k == before: # 앞으로 가는 경우
                            if visit[nx][ny][k] > cnt:
                                visit[nx][ny][k] = cnt
                                queue.append([nx, ny, k, cnt])  
    return minima
        
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
m, n = map(int, stdin.readline().split())
maps = list(list(stdin.readline().rstrip()) for _ in range(n))
room = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'C':
            room.append([i, j])
            
visit = [[[n*m, n*m, n*m, n*m] for _ in range(m)] for _ in range(n)]
visit[room[0][0]][room[0][1]] = [0, 0, 0, 0]
minima = 10**10
print(bfs(room[0][0], room[0][1])-1)