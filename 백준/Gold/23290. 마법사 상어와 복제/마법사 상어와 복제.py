# 23290 마법사 상어와 복제
from sys import stdin
from copy import deepcopy, copy
def shark_move(x, y, cnt, eat, road):
    global eat_maxima, cache
    # 3. 상어가 연속해서 3칸 이동한다. 연속 이동 칸 중 격자를 벗어나면 불가능 
    # 상어가 물고기와 같은 칸으로 가면 먹히고 냄새를 남긴다.
    # 가능한 이동 방법 중 먹히는 물고기 수가 가장 많은 방법으로 이동한다. 
    # 가장 많은 방법이 많으면 사전 순으로 가장 앞서는 방법을 이용한다. 
    if cnt == 3:
        if eat_maxima < eat:
            eat_maxima = eat
            cache = road
        return
    for k in range(4):
        nx, ny = x+sx[k], y+sy[k]
        if 0 <= nx <= 3 and 0 <= ny <= 3:
            temp, fish_num[nx][ny] = fish_num[nx][ny], 0
            shark_move(nx, ny, cnt+1, eat + temp, road + [[nx, ny]])
            fish_num[nx][ny] = temp

m, s = map(int, stdin.readline().split())
dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
sx, sy = [-1, 0, 1, 0], [0, -1, 0, 1] # 상 좌 하 우
fish = []
smell = [[0 for _ in range(4)] for _ in range(4)]
for _ in range(m):
    x, y, d = map(int, stdin.readline().split())
    fish.append([x-1, y-1, d-1, 1])

a, b = map(int, stdin.readline().split())
shark = [a-1, b-1]
while(s):
    # 1. 상어가 모든 물고기에게 복제 마법을 시전 
    copied_fish = deepcopy(fish)
    # 2. 모든 물고기가 한 칸 이동한다. (상어칸 + 물고기 냄새 칸 + 격자 범위 벗어나는 칸 불가)
    # 물고기는 자신이 가지고 있는 방향이 이동할 수 있는 칸을 향할 때까지 반시계 회전한다. 
    fish_num = [[0 for _ in range(4)] for _ in range(4)]     
    for i in range(len(fish)):
        x, y, d, en = fish[i]
        if en:
            cnt = 0
            while(1):
                if cnt > 7:
                    fish_num[x][y] += 1
                    break
                nx, ny = x+dx[d], y+dy[d]
                if  0 <= nx <= 3 and 0 <= ny <= 3 and not smell[nx][ny] and shark != [nx, ny]:
                    fish_num[nx][ny] += 1
                    fish[i] = [nx, ny, d, en]
                    break
                else:
                    d = d - 1
                    if d < 0:
                        d = 7
                    cnt += 1
                    continue

    # 3. 상어가 연속해서 3칸 이동한다. 연속 이동 칸 중 격자를 벗어나면 불가능 
    # 상어가 물고기와 같은 칸으로 가면 먹히고 냄새를 남긴다.
    # 가능한 이동 방법 중 먹히는 물고기 수가 가장 많은 방법으로 이동한다. 
    # 가장 많은 방법이 많으면 사전 순으로 가장 앞서는 방법을 이용한다.
    eat_maxima, cache, eat = -1, [], 0
    x, y = shark
    shark_move(x, y, 0, 0, [])
    for i in range(3): # 동선에 있는 모든 물고기들이 죽는다
        x, y = cache[i]
        for j in range(len(fish)):
            fx, fy = fish[j][0:2]
            if [x, y] == [fx, fy]:
                fish[j][3] = 0
                smell[x][y] = 3 # 두턴 동안 지속되는 물고기의 냄새
    shark = cache[-1] # 마지막 캐시 값은 상어의 새로운 위치

    # 4. 두턴전 연습에서 생긴 물고기의 냄새가 격자에서 사라짐
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    
    # 5. 1에서 사용한 복제마법이 완료된다. 복제된 물고기는 1에서의 위치와 방향을 그대로 가지게 된다. 
    for i in range(len(fish)):
        if fish[i][3]:
            copied_fish.append(fish[i])
    fish = copy(copied_fish)
    s -= 1

print(len(fish))