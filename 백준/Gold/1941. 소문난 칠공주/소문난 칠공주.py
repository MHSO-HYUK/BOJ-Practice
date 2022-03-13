# 1941 소문난 칠공주
from sys import stdin 
def seven(x, y, s, l, road):
    global cnt
    if s + l == 7:
        if s > l:
            cnt += 1
            return       
        
    if l >= 4:
        return

    for k in range(4):
        nx, ny = x +dx[k], y+dy[k]
        if 0<=nx<=4 and 0 <= ny <= 4:
            if (not temp[nx][ny]) and (not visit[nx][ny]) and not sorted(road + [[nx, ny]]) in memory:
                memory.append(sorted(road + [[nx, ny]]))
                if maps[nx][ny] == 'S':
                    temp[nx][ny] = 1
                    seven(nx, ny, s+1, l, road + [[nx, ny]])
                    temp[nx][ny] = 0
                else:
                    temp[nx][ny] = 1
                    seven(nx, ny, s, l+1, road+[[nx, ny]])
                    temp[nx][ny] = 0

    for i in range(5):
        for j in range(5):
            if temp[i][j] and not baam[i][j] and not (i == x and j == y):
                for d in range(4):
                    nx, ny = i + dx[d], j+dy[d]
                    if 0<=nx<=4 and 0 <= ny <= 4:
                        if (not temp[nx][ny]) and (not visit[nx][ny]) and not sorted(road + [[nx, ny]]) in memory:
                            memory.append(sorted(road + [[nx, ny]]))
                            if maps[nx][ny] == 'S':
                                temp[nx][ny] = 1
                                seven(nx, ny, s+1, l, road+[[nx, ny]])
                                temp[nx][ny] = 0
                            else:
                                temp[nx][ny] = 1
                                seven(nx, ny, s, l+1, road+[[nx, ny]])
                                temp[nx][ny] = 0

maps = list(list(stdin.readline().rstrip()) for _ in range(5))
# 총 25명의 학생 -> S // L 로 나뉨
# 7명의 인접한 학생으로 구성되어야  -> S가 4명 이상 포함되어야 한다.
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
visit = [[0]*5 for _ in range(5)]
memory = []
cnt = 0
for i in range(5):
    for j in range(5):
        temp = [[0]*5 for _ in range(5)]
        baam = [[0]*5 for _ in range(5)]
        temp[i][j] = 1
        visit[i][j] = 1
        road = [[i, j]]
        if maps[i][j] == 'S':
            seven(i, j, 1, 0, road)
        else:
            seven(i, j, 0, 1, road)

print(cnt)