# 23290 마법사 상어와 복제
from sys import stdin 
from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)
def shark(x, y, cnt, move_list, eat):
    global move, maxima
    if cnt == 3:
        maxima = max(maxima, eat) # 사전 순으로 마지막에 갱신이 되도록
        if maxima == eat:
            move = move_list
        return
    else:
        for k in range(3, -1, -1):
            nx, ny = x + sx[k], y + sy[k]
            if 0 <= nx <= 3 and 0 <=ny <= 3:
                if fish[nx][ny] and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    shark(nx, ny, cnt+1, move_list+[k], eat+fish[nx][ny])
                    visit[nx][ny] = 0
                if not fish[nx][ny] and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    shark(nx, ny, cnt+1, move_list+[k], eat)
                    visit[nx][ny] = 0
                if visit[nx][ny]:
                    shark(nx, ny, cnt+1, move_list+[k], eat)
                

m, s = map(int, stdin.readline().split())
info = [] #물고기의 위치 + 방향 
fish = [[0]*4 for _ in range(4)] # 물고기의 갯수
for _ in range(m):
    x, y, d = map(int, stdin.readline().split())
    fish[x-1][y-1] += 1
    info.append([x-1, y-1, d-1])
x, y = map(int, stdin.readline().split())
loc = [x-1, y-1] # 상어의 위치 
dx, dy = [0, -1, -1, -1, 0 ,1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1] # 물고기의 이동 
sx, sy = [-1, 0, 1, 0], [0, -1, 0, 1] # 상어의 이동 
smell = [[0]*4 for _ in range(4)] # 물고기의 냄새 
# 4*4 크기의 격자 
# 둘 이상의 물고기가 같은 칸에 있을 수 있고 상어도 같이 있을 수 있음 
count = 0
while(1):
# 1. 상어가 모든 물고기에게 복제 마법을 시전 (5번에서 복제된다.)
    temp = deepcopy(info)
    temp2 = deepcopy(fish)
# 2. 모든 물고기가 한칸 이동하는데 상어가 있거나 물고기의 냄새가 있거나 격자 범위를 벗어나면 불가
# 자신이 가지고 있는 방향이 이동할 수 있는 칸을 향할 때 까지 방향이 반시계로 돌아감
    fish = [[0]*4 for _ in range(4)]
    for i in range(len(info)):
        if info[i]: # 살아있다면 
            x, y, d = info[i]
            ds = d # 초기 방향값 
            while(1):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx <= 3 and 0<= ny <= 3:
                    if loc != [nx, ny] and not smell[nx][ny]: # 냄새가 없거나 상어가 없는 경우
                        info[i] = [nx, ny, d]
                        fish[nx][ny] += 1
                        break
                    else:
                        d -= 1
                        if d < 0:
                            d += 8
                        if ds == d: # 초기 방향값까지 한바퀴 돈 경우
                            fish[x][y] += 1
                            break
                else:
                    d -= 1
                    if d < 0 :
                        d += 8
                    if ds == d: # 초기 방향값까지 한바퀴 돈 경우
                        fish[x][y] += 1
                        break
# 3. 상어가 연속해서 3칸을 이동한다. 격자의 범위를 벗어나지 못하고 이동 중 물고기가 있다면 먹어버림 
# 먹힌 물고기는 냄새를 남긴다. -> 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동
# 그런 방법이 많으면 사전 순으로 가장 앞서는 방법을 이용
    maxima, move = -1, []
    visit = [[0]*4 for _ in range(4)]
    shark(loc[0], loc[1], 0, [], 0) # move 변수에 상어가 이동하는 길을 저장하도록 함

    x, y = loc[0], loc[1]
    for i in range(len(move)):
        k = move[i]
        nx, ny = x+sx[k], y+sy[k]
        if fish[nx][ny]: # 물고기가 잡아먹힘
            fish[nx][ny] = 0
            smell[nx][ny] = 3 # 두턴 동안 냄새는 남아있는다.
            for j in range(len(info)):
                if info[j]:
                    if (info[j][0], info[j][1]) == (nx, ny):
                        info[j] = 0
        x, y = nx, ny
    loc = [x, y]
    
# 4. 2회 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1
                
# 5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 됨. 
    for i in range(4):
        for j in range(4):
            fish[i][j] += temp2[i][j]
    
    pocket = []
    for i in range(len(info)): # 죽은 물고기 건져내기
        if info[i]:
            pocket.append(info[i])
    info = deepcopy(pocket)
    info = info + temp
    
    count += 1
    if count == s: # s번 마법 사용시 종료
        break
        
print(sum(map(sum,fish)))