# 20061 모노미노도미노 2
from sys import stdin
from collections import deque
def drop_tile(t, x, y):
    # 1. 타일이 떨어진다. 
    if t == 1: #초록 // (x, y)  파랑 // (y, x)
        for i in range(7):
            if i == 6 or green[i][y]: # 블럭이 있거나 바닥인 경우
                break
        green[i-1][y] = 1
        for i in range(7):
            if i == 6 or blue[x][i]: # 블럭이 있거나 바닥인 경우
                break
        blue[x][i-1] = 1
    elif t == 2: # 초록 // (x, y, y+1)   파랑 // (y, y+1 / x)
        for i in range(7):
            if i == 6 or green[i][y] or green[i][y+1]: # 블럭이 있거나 바닥인 경우
                break
        green[i-1][y], green[i-1][y+1] = 1, 1
        for i in range(7):
            if i == 6 or blue[x][i] or blue[x][i]: # 블럭이 있거나 바닥인 경우
                break
        blue[x][i-1], blue[x][i-2] = 1, 1
    else: # 초록 // (x, x+1, y)  파랑 // (y, x, x+1) 
        for i in range(7):
            if i == 6 or green[i][y]: # 블럭이 있거나 바닥인 경우
                break
        green[i-1][y], green[i-2][y] = 1, 1
        for i in range(7):
            if i == 6 or blue[x][i] or blue[x+1][i]: # 블럭이 있거나 바닥인 경우
                break
        blue[x][i-1], blue[x+1][i-1] = 1, 1

        
def check_line():
    global score, green, blue, flag
    gflag, bflag = 0, 0
    gcheck = []
    for i in range(5, -1, -1):
        if sum(green[i]) == 4:
            gcheck.append(i)
    
    cnt = 0
    for i in gcheck:
        i += cnt
        score += 1
        green = [[0, 0, 0, 0]] + green[0:i] + green[i+1:6]
        cnt += 1
    
    if sum(green[0]): 
        gflag = 2
    elif sum(green[1]):
        gflag = 1
    
    bcheck = []
    for j in range(5, -1, -1):
        s = 0
        for i in range(4):
            s += blue[i][j]
        if s == 4:
            bcheck.append(j)
    
    cnt = 0
    for j in bcheck:
        j += cnt
        score += 1
        for a in range(4):
            blue[a] = [0] + blue[a][0:j] + blue[a][j+1:6]
        cnt += 1
    
    for i in range(2):
        for j in range(4):
            if blue[j][i]:
                if i == 0:
                    bflag = 2
                elif bflag == 0 and i == 1:
                    bflag = 1
        
    if gflag:
        if gflag == 1:
            green = [[0, 0, 0, 0]] + green[0:5]
        else:
            green = [[0, 0, 0, 0] for _ in range(2)] + green[0:4]

    if bflag:
        if bflag == 1:
            for a in range(4):
                blue[a] = [0] + blue[a][0:5]
        else:
            for a in range(4):
                blue[a] = [0, 0] + blue[a][0:4]

n = int(stdin.readline())
comm = deque()
for _ in range(n):
    comm.append(list(map(int, stdin.readline().split())))

# 하나의 행이 타일로 가득 차면 사라진다. 
# 그 위에 있던 타일들이 한 칸씩 떨어짐 + 점수는 사라진 줄의 수만큼 획득한다. 
# 0, 1번 행에 블록이 들어가면 해당 행만큼 사라진다. 
green, blue = [[0 for _ in range(4)] for _ in range(6)], [[0 for _ in range(6)] for _ in range(4)]
score = 0
while(comm):
    t, x, y = comm.popleft()
    drop_tile(t, x, y)
    # 2. 초록과 파랑 중 한줄이 만들어진 것이 있다면 터트리고 그 위의 타일을 한칸씩 떨군다.
    # 3. 맨위 두줄에 타일이 있다면 해당 줄만큼 아래에서 빼준다. 
    check_line()

    
print(score)
print(sum(map(sum, blue)) + sum(map(sum, green)))