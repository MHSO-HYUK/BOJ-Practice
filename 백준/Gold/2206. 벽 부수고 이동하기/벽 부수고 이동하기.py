#2206 벽부수고 이동하기
from collections import deque
def road_find(maps):
    queue = deque([[0,0,0]])
    visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visit[0][0][0] = 1
    dx, dy = [1,-1,0,0],[0,0,1,-1]
    while(queue):
            x, y, c = queue.popleft()
            if(x == n-1 and y == m-1):
                return visit[x][y][c]
            for i in range(4):
                a, b = x+dx[i], y+dy[i]
                if(0<=a<n and 0<=b<m):
                    if(maps[a][b] == 0 and visit[a][b][c] == 0):
                        visit[a][b][c] = visit[x][y][c] + 1
                        queue.append([a,b,c])
                    if(maps[a][b] == 1 and c == 0):
                        visit[a][b][c+1] = visit[x][y][c] +1
                        queue.append([a,b,c+1])
    return -1
        
n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input())))
    
print(road_find(maps))