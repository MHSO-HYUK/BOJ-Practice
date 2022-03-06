# 14890 경사로
from sys import stdin 
n, l = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
# 지도의 각칸은 높이 - 지나갈 수 있는 길이 몇개인지 알아보자
# 길이란 한쪽 끝에서 다른쪽 끝까지 지나가는 것을 말한다.
# 길을 지나가기 위해서는 모든 칸의 높이가 같거나 경사로를 높아서 지나갈 수 있는 길을 만들수 있는 경우
# 경사로는 낮은 칸에 놓으며 l개의 연속된 칸에 바닥이 모두 접해야 한다. 
# 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
def go(x, y, d):
    global flag
    if (not (0 <= x+dx[d] <= n-1)) or (not (0<= y+dy[d] <= n-1)):
        flag = True
    
    elif 0 <= x <= n-1 and 0 <= y <= n-1:
        if maps[x][y] == maps[x+dx[d]][y+dy[d]]: # 평지
            go(x+dx[d], y+dy[d], d)
        
        else: # NOT 평지
            if abs(maps[x][y] -maps[x+dx[d]][y+dy[d]]) == 1: 
                if 0 <= x + l * dx[d] <= n-1 and 0 <= y + l * dy[d] <= n-1:
                    if maps[x][y] > maps[x+dx[d]][y+dy[d]]: # 1 차이가 나는 내리막길 
                        for i in range(1, l+1):
                            if road[x+i*dx[d]][y+i*dy[d]] or maps[x+i*dx[d]][y+i*dy[d]] != maps[x+dx[d]][y+dy[d]] : # l 동안 높이 차가 나버리는 경우
                                return 0
                            road[x+i*dx[d]][y+i*dy[d]] = 1
                        go(x+l*dx[d], y+l*dy[d], d)
                        
                    else:# 1 차이가 나는 오르막길
                        if 0 <= x-(l-1)*dx[d] <= n-1 and 0<=y - (l-1)*dy[d] <= n-1:                             
                            for i in range(l):
                                if road[x-i*dx[d]][y-i*dy[d]] or maps[x-i*dx[d]][y-i*dy[d]] != maps[x][y] : # l 동안 높이 차가 나버리는 경우
                                    return 0
                                road[x-i*dx[d]][y-i*dy[d]] = 1
                            go(x+dx[d], y+dy[d], d)
                        else:
                            return 0
                else:
                    return 0
                
    if flag:
        return 1
    else:
        return 0
    
cnt = 0
visit = [[[0]*4 for _ in range(n)] for _ in range(n)]
for i in range(n):
    flag = False
    temp = cnt
    road =  [[0 for _ in range(n)] for _ in range(n)]
    cnt += go(i, 0, 0) #오른쪽
    if cnt != temp:
        visit[i][0][0] = 1
    flag = False
    if not visit[i][0][0]:
        temp = cnt
        road =  [[0 for _ in range(n)] for _ in range(n)]
        cnt += go(i, n-1, 1) # 왼쪽
            
for j in range(n):
    flag = False
    temp = cnt
    road =  [[0 for _ in range(n)] for _ in range(n)]
    cnt += go(0, j, 2) # 아래쪽
    if cnt != temp:
        visit[0][j][2] = 1
    flag = False
    if not visit[0][j][2]:
        temp = cnt
        road =  [[0 for _ in range(n)] for _ in range(n)]
        cnt += go(n-1, j, 3) # 위쪽

print(cnt)