#15685 드래곤 커브
from sys import stdin 
n = int(stdin.readline())
info = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
# k세대 드래곤 커브는 k-1세대 드래곤 커브를 끝점을 기존으로 90도 시계방향으로 돌리고 
# 그것을 k-1세대 드래곤 커브의 끝점에 붙힌것
# info // x, y, d 시작방향, g 세대 
# 드래곤 커브는 격자 밖으로 벗어나지 않고 겹칠 수 있다!
def rotate():
    global move, last
    temp = []
    for i in range(len(move)-1, -1, -1):
        if move[i] == 0: # 우
            visit[last[0] + dx[1]][last[1] + dy[1]] = 1
            last = [last[0] + dx[1], last[1] + dy[1]]
            temp.append(1)
            
        elif move[i] == 1: # 위
            visit[last[0] + dx[2]][last[1] + dy[2]] = 1
            last = [last[0] + dx[2], last[1] + dy[2]]
            temp.append(2)
            
        elif move[i] == 2: # 좌
            visit[last[0] + dx[3]][last[1] + dy[3]] = 1
            last = [last[0] + dx[3], last[1] + dy[3]]
            temp.append(3)
            
        elif move[i] == 3: # 아래 
            visit[last[0] + dx[0]][last[1] + dy[0]] = 1
            last = [last[0] + dx[0], last[1] + dy[0]]
            temp.append(0)
            
    move = move + temp
    
def dragon(x, y, d, g):
    global last, move
    if g == 0:
        visit[x][y], visit[x+dx[d]][y+dy[d]] = 1, 1
        move.append(d)
        last = [x+dx[d], y+dy[d]] 
    else:
        dragon(x, y, d, g-1)
        rotate() 
        

n_visit = [[0]* 101 for _ in range(101)]
for i in range(n):
    visit = [[0]* 101 for _ in range(101)]
    x, y, d, g = info[i]
    last = []
    move = []
    dragon(y, x, d, g)
    for i in range(101):
        for j in range(101):
            if visit[i][j]:
                n_visit[i][j] = 1
                
cnt = 0
for i in range(101):
    for j in range(101):
        if 1 <= i+1 <= 100 and 1 <= j+1 <= 100:
            if n_visit[i][j] and n_visit[i+1][j] and n_visit[i][j+1] and n_visit[i+1][j+1]:
                cnt += 1
print(cnt)