# 17837 새로운 게임 2
from sys import stdin
import sys

n, k = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
state = [[[] for _ in range(n)] for _ in range(n)]
info = []
dx, dy =[0, 0, -1, 1], [1, -1, 0, 0]
for i in range(k):
    r, c, d = map(int, stdin.readline().split())
    info.append([r-1, c-1, d-1])
    state[r-1][c-1].append(i)
turn = 1
while(1):
    # 턴 한번은 1 ~ 말 이동 // 0 흰 1 빨 2 파
    for i in range(k):
        x, y, d = info[i]
        nx, ny = x+dx[d], y+dy[d]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1:
            # 흰색 -> 이동 (이미 있다면 가장 위에 올림)
            if maps[nx][ny] == 0:
                    for j in range(len(state[x][y])):
                        if state[x][y][j] == i: 
                            break
                    for z in range(j, len(state[x][y])):
                        info[state[x][y][z]][0], info[state[x][y][z]][1] = nx, ny
                    state[nx][ny] = state[nx][ny] + state[x][y][j:]
                    state[x][y] = state[x][y][0:j]
                    if len(state[nx][ny]) >= 4: 
                        print(turn)
                        sys.exit()
                    continue
            
            # 빨강 -> 이동하고 반대로 돌림
            if maps[nx][ny] == 1:
                for j in range(len(state[x][y])):
                    if state[x][y][j] == i: 
                        break
                for z in range(j, len(state[x][y])):
                    info[state[x][y][z]][0], info[state[x][y][z]][1] = nx, ny
                state[nx][ny] = (state[nx][ny]) + (state[x][y][j:])[::-1]
                state[x][y] = state[x][y][0:j]   
                if len(state[nx][ny]) >= 4: 
                        print(turn)
                        sys.exit()
                continue
        
        # 파랑 or 범위 밖 -> A의 이동방향을 반대로 하고 한칸 이동 (파랑 or 범위 밖이면 이동 X)
        if not (0 <= nx <= n-1 and 0 <= ny <= n-1) or maps[nx][ny] == 2 :
            if info[i][2] == 0:
                info[i][2] = 1
            elif info[i][2] == 1:
                info[i][2] = 0
            elif info[i][2] == 2:
                info[i][2] = 3
            else:
                info[i][2] = 2
                
            x, y, d = info[i]
            nx, ny = x + dx[d], y+dy[d]
            if not (0 <= nx <= n-1 and 0 <= ny <= n-1) or maps[nx][ny] == 2:
                pass
            else:
                if maps[nx][ny] == 0:
                    for j in range(len(state[x][y])):
                        if state[x][y][j] == i: 
                            break
                    for z in range(j, len(state[x][y])):
                        info[state[x][y][z]][0], info[state[x][y][z]][1] = nx, ny
                    state[nx][ny] = state[nx][ny] + state[x][y][j:]
                    state[x][y] = state[x][y][0:j]
                    if len(state[nx][ny]) >= 4: 
                        print(turn)
                        sys.exit()
                    continue
            
                # 빨강 -> 이동하고 반대로 돌림
                if maps[nx][ny] == 1:
                    for j in range(len(state[x][y])):
                        if state[x][y][j] == i: 
                            break
                    for z in range(j, len(state[x][y])):
                        info[state[x][y][z]][0], info[state[x][y][z]][1] = nx, ny
                    state[nx][ny] = (state[nx][ny]) + (state[x][y][j:])[::-1]
                    state[x][y] = state[x][y][0:j]
                    if len(state[nx][ny]) >= 4: 
                        print(turn)
                        sys.exit()
                    continue
    turn += 1
    if turn > 1000:
        break
print(-1)