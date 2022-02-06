#16954 움직이는 미로 탈출
# 1초마다 모든 벽이 아래에 있는 행으로 한칸씩 내려감
# 캐릭터 이동 -> 벽이동  (반복)
# 벽이 캐릭터 있는 칸으로 이동할 경우 캐릭터 이동 불가
# 왼쪽 아래 -> 오른쪽 위로 이동해야
import sys
from sys import stdin
sys.setrecursionlimit(10**6)

def miro(x, y, maps, flag):
    if(x== 0 and y == 7):
        print(1)
        sys.exit()
    if(maps[x][y] != '#' and flag < 8):
        for k in range(9):
            a, b  = x + dx[k], y + dy[k]
            if(0<=a<=7 and 0<=b<=7):
                if(maps[a][b] != '#'):
                    if(visit[a][b] == 0):
                        visit[a][b] = 1
                        miro(a, b, wall(maps), flag)
                        visit[a][b] = 0
                    if(k == 7):
                        miro(a, b, wall(maps), flag + 1)
    if(x == 7 and y == 0):
        print(0)
        sys.exit()
        
def wall(maps):
    temp = [['.']*8]
    for i in range(7):
        temp.append(maps[i])
    return temp
    
maps = []
for _ in range(8):
    maps.append(list(stdin.readline().rstrip()))
dx, dy = [1, 1, 1, -1, -1, -1, 0, 0 ,0], [1, 0, -1, 1, 0, -1, 1, 0, -1]
visit = [[0]*8 for _ in range(8)]
visit[7][0] = 1
miro(7, 0, maps, 0)
