# 20061 모노미노도미노2
from sys import stdin 
from copy import deepcopy
n = int(stdin.readline())
info = []
for _ in range(n):
    t, x, y = map(int, stdin.readline().split())
    info.append([x, y, t])
info.reverse()
# 블록을 빨간색에 넣으면 그 위치부터 경계에 닿거나 타 블록에 닿을 떄까지 이동한다.
# 어떤 보드의 행이 타일로 가득 찬다면 그 행의 타일은 모두 사라진다. 
# 점수는 하나의 행이나 열이 터질때 마다 추가된다, 
# 사라진 이후에는 테트리스 마냥 떨어진다. 

# 이 경우에는 점수 없음 
# 초록보드의 0, 1번 행에 블록이 있으면 블록이 있는 행의 수만큼 아래 행에 있는 타일이 사라지고 떨어짐
#파란보드의 0, 1 열에 블록이 있으면 블록이 있는 열의 수만큼 오른쪽 열이 사라지고 떨어짐 
def blue_block(maps):
    global score, blue
    temp = []
    now = [[0 for _ in range(4)] for _ in range(6)]
    for i in range(len(maps)):
        y = maps[i][0]
        if not now[0][y]:
            now[0][y] = 1
            temp.append([0, y])
        elif now[0][y]: # 2*1칸일 때 발생 가능 
            now[1][y] = 1
            temp.append([1, y])
    
    flag = False
    while(1):
        if flag:
            break
        maps = []
        for i in range(len(temp)):
            x, y = temp[i][0], temp[i][1]
            nx, ny = x + dx[0], y + dy[0]
            if 0 <= nx <= 5 and 0 <= ny <= 3:
                if blue[nx][ny] == 1: # 한칸 더 가면 겹침
                    flag = True
                else:
                    x, y = nx, ny
                    maps.append([x, y])
            else:
                flag = True   
                
        if not flag: # 겹치지 않았음 
            temp = deepcopy(maps)
            
        else: # 겹쳐버렸음 -> temp가 새로운 블럭의 최종 목적지가 됌 
            for i in range(len(temp)):
                blue[temp[i][0]][temp[i][1]] = 1
    
    while(1):
        bflag = False     
        bang = []
        for i in range(5, -1, -1):
            if sum(blue[i]) == 4: # 모든 행이 차게 되면
                bflag = True
                bang.append(i)
                blue[i] = [0, 0, 0, 0] # 터짐 
                score += 1
        
        if not bflag:
            break
        else:
            b = [0 for _ in range(6)]
            for k in bang: # 행이 터진 경우에는
                
                blue[k] = [0, 0, 0, 0]
                b[k] = 1
                
        for i in range(6):
            if b[i] == 1: # i 행이 터진 행이라면 
                blue[0:i+1]  = [[0, 0, 0, 0]] + blue[0:i]
                
                
    cnt = 0    
    for i in range(0, 2): 
        if blue[i] != [0, 0, 0, 0]:
            cnt += 1
    if cnt == 0:
        pass
    elif cnt == 1:
        blue =  [[0, 0, 0, 0]] +  blue[0:5]
    else:
        blue = [[0, 0, 0, 0]] + [[0, 0, 0, 0]]  + blue[0:4]

        
        
def green_block(maps):
    global score, green
    temp = []
    now = [[0 for _ in range(4)] for _ in range(6)]
    for i in range(len(maps)):
        y = maps[i][1]
        if not now[0][y]:
            now[0][y] = 1
            temp.append([0, y])
        elif now[0][y]: # 2*1칸일 때 발생 가능 
            now[1][y] = 1
            temp.append([1, y])
    flag = False
    
    while(1):
        if flag:
            break
        maps = []
        for i in range(len(temp)):
            x, y = temp[i][0], temp[i][1]
            nx, ny = x + dx[0], y + dy[0]
            if 0 <= nx <= 5 and 0 <= ny <= 3:
                if green[nx][ny] == 1: # 한칸 더 가면 겹침
                    flag = True
                else:
                    x, y = nx, ny
                    maps.append([x, y])
            else:
                flag = True   
                
        if not flag: # 겹치지 않았음 
            temp = deepcopy(maps) # temp 최적화
            
        else: # 겹쳐버렸음 -> temp가 새로운 블럭의 최종 목적지가 됌 
            for i in range(len(temp)):
                green[temp[i][0]][temp[i][1]] = 1
    
    while(1):
        bflag = False     
        bang = []
        for i in range(5, -1, -1):
            if sum(green[i]) == 4: # 모든 행이 차게 되면
                bflag = True
                bang.append(i)
                green[i] = [0, 0, 0, 0] # 터짐 
                score += 1
        
        if not bflag:
            break
        else:
            b = [0 for _ in range(6)]
            for k in bang: # 행이 터진 경우에는
                green[k] = [0, 0, 0, 0]
                b[k] = 1
                
        for i in range(6):
            if b[i] == 1: # i 행이 터진 행이라면 
                green[0:i+1]  = [[0, 0, 0, 0]] + green[0:i]
                
    cnt = 0    
    for i in range(0, 2): 
        if green[i] != [0, 0, 0, 0]: # 연한 부분에 블럭이 있는 경우
            cnt += 1
    if cnt == 0:
        pass
    elif cnt == 1:
        green =  [[0, 0, 0, 0]] + green[0:5]
    else:
        green =  [[0, 0, 0, 0]] + [[0, 0, 0, 0]] + green[0:4]
                
            
             
# 두 케이스가 동시에 존재하는 경우 -> 점수 획득 과정이 우선이다
blue = [[0 for _ in range(4)] for _ in range(6)]
green = [[0 for _ in range(4)] for _ in range(6)]
score = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
while(info):
    x, y, t = info.pop()
    if t == 1: # t = 1  -> x, y 
        blue_block([[x, y]])
        green_block([[x, y]])
        
    elif t == 2: # t = 2 -> x,y x,y+1
        blue_block([[x, y], [x, y+1]])
        green_block([[x, y], [x, y+1]])
        
    else: # t = 3 -> x, y x+1, y
        blue_block([[x, y], [x+1, y]])
        green_block([[x, y], [x+1, y]])
    
print(score)
print(sum(map(sum, blue)) + sum(map(sum, green)))