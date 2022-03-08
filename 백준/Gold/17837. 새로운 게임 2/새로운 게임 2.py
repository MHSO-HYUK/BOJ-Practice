# 17837 새로운 게임 2
from sys import stdin
from collections import deque
import sys 

n, num = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
info = []
visit = [[[] for _ in range(n)] for _ in range(n)]
for i in range(num):
    x, y, d = map(int, stdin.readline().split())
    info.append([x-1, y-1, d])
    visit[x-1][y-1].append(i)

dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
turn = 1
while(1):
    if turn > 1000:
        print(-1)
        sys.exit()
        
    for i in range(num):        
        x, y, d = info[i]
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1:
            if maps[nx][ny] == 0: # 흰색이면 그 칸으로 이동 // 말이 이미 있다면 그 위에 A를 올림
                temp = deque()
                while(1):
                    k = visit[x][y].pop()
                    info[k][0], info[k][1] = nx, ny
                    temp.appendleft(k)
                    if k == i :
                        break
                visit[nx][ny] = visit[nx][ny] + list(temp)
                if len(visit[nx][ny]) >= 4:
                    print(turn)
                    sys.exit()

            elif maps[nx][ny] == 1: # 빨간색이면 이동한 후에 A번 말과 그 위의 모든 말의 쌓인 순서를 반대로 바꾼다
                temp = deque()
                while(1):
                    k = visit[x][y].pop()
                    info[k][0], info[k][1] = nx, ny
                    temp.append(k)
                    if k == i :
                        break
                visit[nx][ny] = visit[nx][ny] + list(temp)
                if len(visit[nx][ny]) >= 4:
                    print(turn)
                    sys.exit()
                
            elif maps[nx][ny] == 2: 
            # 파란색이면 A번 말의 이동방향을 반대로 하고 한칸 이동한다. 
            # 이때 방향을 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
            # 체스판을 벗어나는 경우는 파란색과 같다. 
                if d % 2: 
                    d += 1
                else:
                    d -= 1
                info[i][2] = d
                bx, by = x + dx[d], y + dy[d]
                if 0<= bx <= n-1 and 0 <= by <= n-1:
                    if maps[bx][by] == 0:
                        temp = deque()
                        while(1):
                            k = visit[x][y].pop()
                            info[k][0], info[k][1] = bx, by
                            temp.appendleft(k)
                            if k == i :
                                break
                        visit[bx][by] = visit[bx][by] + list(temp)
                        if len(visit[bx][by]) >= 4:
                            print(turn)
                            sys.exit()
                            
                    elif maps[bx][by] == 1:
                        temp = deque()
                        while(1):
                            k = visit[x][y].pop()
                            info[k][0], info[k][1] = bx, by
                            temp.append(k)
                            if k == i :
                                break
                        visit[bx][by] = visit[bx][by] + list(temp)
                        if len(visit[bx][by]) >= 4:
                            print(turn)
                            sys.exit()
                                     
        else: # 칸을 벗어나는 경우 = 파랑 
            if d % 2:
                d += 1
            else:
                d -= 1
            info[i][2] = d
            bx, by = x + dx[d], y + dy[d]
            if 0<= bx <= n-1 and 0 <= by <= n-1:
                if maps[bx][by] == 0:
                    temp = deque()
                    while(1):
                        k = visit[x][y].pop()
                        info[k][0], info[k][1] = bx, by
                        temp.appendleft(k)
                        if k == i :
                            break
                    visit[bx][by] = visit[bx][by] + list(temp)
                    if len(visit[bx][by]) >= 4:
                        print(turn)
                        sys.exit()
                        
                elif maps[bx][by] == 1:
                        temp = deque()
                        while(1):
                            k = visit[x][y].pop()
                            info[k][0], info[k][1] = bx, by
                            temp.append(k)
                            if k == i :
                                break
                        visit[bx][by] = visit[bx][by] + list(temp)
                        if len(visit[bx][by]) >= 4:
                            print(turn)
                            sys.exit()

    turn += 1
# 방향 1 우 2 좌 3 위 4 아래
# 색깔 0 흰 1 빨 2 파