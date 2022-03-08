# 19236 청소년 상어
from sys import stdin 
from copy import deepcopy
def fish():
    global sloc
    # 이동 가능한 칸은 빈칸과 다른 물고기가 있는 칸
    # 상어가 있거나, 경계를 넘으면 불가
    # 이동이 가능할때까지 45도 반시계 회전 (없으면 X)
    # 물고기끼리 위치 교환 가능
    for i in range(1, 17):
        if dirc[i]: # 살아있다면
            ds = dirc[i]
            d = ds
            x, y = loc[i]
            while(1):
                flag = False
                nx, ny = x+dx[d], y + dy[d]
                if 0 <= nx <= 3 and 0 <=ny <= 3:
                    if sloc != [nx, ny]: # 상어의 위치가 아니라면
                        flag = True
                        if maps[nx][ny] == 0: # 빈칸이라면
                            maps[x][y] = 0
                            maps[nx][ny] = i
                            dirc[i] = d
                            loc[i] = [nx, ny]
                        else: # 다른 고기가 있다면
                            maps[x][y], maps[nx][ny] = maps[nx][ny], maps[x][y]
                            loc[i] = [nx, ny]
                            loc[maps[x][y]] = [x, y]
                            dirc[i] = d
                if flag: # 이동완료
                    break
                else:
                    d += 1
                    if d > 8:
                        d %= 8
                    if d == ds:
                        break
                        
def shark(x, y, d, score, t): # 물고기가 없는 칸으로는 이동 불가
    global maxima, sloc, maps, loc, dirc, sdirc
    fish()
    eat = False
    temp = deepcopy(maps)
    temp2 = deepcopy(loc)
    temp3 = deepcopy(dirc)
    temp4 = sloc
    temp5 = sdirc
    # 변경 이전의 맵 값 저장
    for s in range(1, 4):
        maps = deepcopy(temp)
        loc = deepcopy(temp2)
        dirc = deepcopy(temp3)
        sloc = temp4
        sdirc = temp5

        sx, sy = x + s*dx[sdirc], y + s*dy[sdirc]
        if 0 <= sx <= 3 and 0 <= sy <= 3:
            if maps[sx][sy]:
                eat = True    
                score += maps[sx][sy]
                sdirc = dirc[maps[sx][sy]]
                dirc[maps[sx][sy]] = 0
                maps[sx][sy] = 0
                sloc = [sx, sy]
                shark(sx, sy, sdirc, score, t + 1)
                score -= temp[sx][sy]
                
        
    if not eat: # 길이 막힌 경우
        maxima = max(maxima, score)

    
# 상어는 (0, 0) 물고기를 먹고 들어감(방향도 흡수)
# 이후 물고기가 이동(번호가 작은 물고기 순서대로, 한칸 이동 가능)
# 물고기 이동 끝나면 상어 이동(한번에 여러칸 이동 가능)
dirc = [0 for _ in range(17)]
loc = [[] for _ in range(17)]
maps = [[0]*4 for _ in range(4)]
for i in range(4):
    a, b, c, d, e, f, g, h = map(int, stdin.readline().split())
    dirc[a], loc[a] = b, [i, 0]
    maps[i][0] = a
    dirc[c], loc[c] = d, [i, 1]
    maps[i][1] = c
    dirc[e], loc[e] = f, [i, 2]
    maps[i][2] = e
    dirc[g], loc[g] = h, [i, 3]
    maps[i][3] = g

dx, dy = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, -1, -1, -1, 0, 1, 1, 1] # 1 ~ 8사이 자연수 방향
# 초기 상태 적립

sloc, sdirc, score = [0,0], dirc[maps[0][0]], maps[0][0]
dirc[maps[0][0]] = 0
maps[0][0] = 0
maxima = 0
shark(0, 0, sdirc, score, 0)
print(maxima)