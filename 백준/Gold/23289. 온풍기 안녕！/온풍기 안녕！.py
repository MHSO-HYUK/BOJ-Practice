# 23289 온풍기 안녕!
from sys import stdin 
from collections import deque
def spread(x, y, d):
    visit = [[0]*m for _ in range(n)]
    queue = deque([[x, y, 4]])
    visit[x][y] = 1
    while(queue):
        x, y, p = queue.popleft()
        if p == 0:
            return
        for k in range(3):
            nx, ny = x + move[d][0][k], y + move[d][1][k]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if not visit[nx][ny]:
                    if k == 0 or k == 2: # 대각선 바람
                        if d== 0 or d == 1: # 좌우 바람
                            if not wall[nx][y][nx][ny] and not wall[nx][y][x][y]:
                                visit[nx][ny] = 1
                                tem[nx][ny] += p
                                queue.append([nx, ny, p-1])
                                
                        elif d == 2 or d == 3: # 상하 바람 
                            if not wall[x][y][x][ny] and not wall[x][ny][nx][ny]:
                                visit[nx][ny] = 1
                                tem[nx][ny] += p
                                queue.append([nx, ny, p-1])
                                
                    else: # 직선 바람
                        if not wall[x][y][nx][ny]:
                            visit[nx][ny] = 1
                            tem[nx][ny] += p
                            queue.append([nx, ny, p-1])
                           
def wind():
    # 1. 집에 있는 모든 온풍기에서 바람이 한번 나옴 
    # 2대 이상 있을 경우 온도의 합
    # 벽이 있으면 흐름이 끊김
    # 온풍기가 있는 칸도 온도를 가질 수 있음
    for i in range(len(fan)):
        queue = deque()
        x, y, d = fan[i]   
        if d == 1: # 1 오른쪽 
            nx, ny = x + dx[2], y + dy[2] # 한칸 앞으로
            if 0 <= nx <= n-1 and 0<= ny <= m-1:
                if not wall[x][y][nx][ny]:
                    tem[nx][ny] += 5
                    spread(nx, ny, d-1)
            
        elif d == 2: # 2 왼쪽
            nx, ny = x + dx[3], y + dy[3]
            if 0 <= nx <= n-1 and 0<= ny <= m-1:
                if not wall[x][y][nx][ny]:
                    tem[nx][ny] += 5
                    spread(nx, ny, d-1)
            
        elif d == 3: # 3 위쪽
            nx, ny = x + dx[1], y + dy[1]
            if 0 <= nx <= n-1 and 0<= ny <= m-1:
                if not wall[x][y][nx][ny]:
                    tem[nx][ny] += 5
                    spread(nx, ny, d-1)
            
        elif d == 4: # 4 아래쪽
            nx, ny = x + dx[0], y + dy[0]
            if 0 <= nx <= n-1 and 0<= ny <= m-1:
                if not wall[x][y][nx][ny]:
                    tem[nx][ny] += 5
                    spread(nx, ny, d-1)
            
n, m, go = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split()))for _ in range(n))
w = int(stdin.readline())
tem = [[0]*m for _ in range(n)]
wall = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
for _ in range(w):
    x, y, t = map(int, stdin.readline().split())
    x, y = x-1, y-1
    if t == 0:
        wall[x-1][y][x][y] = 1
        wall[x][y][x-1][y] = 1
    else:
        wall[x][y][x][y+1]= 1
        wall[x][y+1][x][y] = 1
        
fan, ask = [], []
for i in range(n):
    for j in range(m):
        if 1 <= maps[i][j] <= 4:
            fan.append([i, j, maps[i][j]])
        if maps[i][j] == 5:
            ask.append([i, j])
            
move = [[[1, 0,-1], [1, 1, 1]], [[1, 0, -1], [-1, -1, -1]], [[-1, -1, -1], [1, 0, -1]], [[1, 1, 1], [1, 0, -1]]] #우 좌 상 하
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1] # 하 상 우 좌
choco = 0
while(1):
    wind()
    
# 2. 온도가 조절됨
# 모든 인접한 칸에 대해서 온도가 높은 칸에서 낮은 칸으로 {온도의 차이 // 4} 만큼 온도가 조절 (-, +)
# 벽이 사이에 있는 경우에는 조절 X
    change = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx <= n-1 and 0<= ny <= m-1:
                    if not wall[x][y][nx][ny]: # 사이에 벽이 없을 경우 
                        if tem[x][y] < tem[nx][ny]:
                            change[x][y] += (tem[nx][ny] - tem[x][y]) // 4
                            
                        elif tem[x][y] > tem[nx][ny]:
                            change[x][y] -= (tem[x][y] - tem[nx][ny]) // 4

    for i in range(n):
        for j in range(m):
            tem[i][j] += change[i][j]
            
# 3. 온도가 1 이상인 가장 바깥쪽의 온도가 1씩 감소
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n-1 or j == m-1:
                if tem[i][j]:
                    tem[i][j] -= 1
                
# 4. 초콜릿을 하나 먹음
    choco += 1
    if choco > 100:
        break
        

# 5. 조사하는 모든 칸의 온도가 K도 이상이 되었는지 검사 // 아니라면 반복
    flag = True
    for i in range(len(ask)):
        x, y = ask[i]
        if tem[x][y] < go:
            flag = False
            break
    if flag:
        break
        
print(choco)