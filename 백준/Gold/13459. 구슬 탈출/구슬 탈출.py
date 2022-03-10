# 13459 구슬 탈출 
from sys import stdin
import sys
sys.setrecursionlimit(10**5)
def escape(red, blue, cnt, before):
    if cnt >= 10:
        return
    for k in range(4):
        if k != before:
            x, y = red
            i, j = blue
            a, b, c, d = x, y, i, j
            rflag, bflag = False, False
            while(1):
                nx, ny = x+dx[k], y +dy[k]
                if maps[nx][ny] == '#':
                    break
                elif maps[nx][ny] == 'O':
                    rflag = True
                    break
                else:
                    x, y = nx, ny
                    
            while(1):
                ni, nj = i+dx[k], j +dy[k]
                if maps[ni][nj] == '#':
                    break
                elif maps[ni][nj] == 'O':
                    bflag = True
                    break
                else:
                    i, j = ni, nj
                  
            if rflag and not bflag:
                print(1)
                sys.exit()
            
            elif (not rflag) and (not bflag):
                if [x, y] == [i, j]:
                    if a == c: 
                        if k == 2: # 우
                            s = True if b > d else False
                        if k == 3:
                            s = True if b < d else False
                    if b == d:
                        if k == 0:
                            s = True if a > c else False
                        if k == 1:
                            s = True if a < c else False
                    
                    if s :
                        escape([x, y], [i-dx[k], j-dy[k]], cnt+1, k)
                    else:
                        escape([x-dx[k], y-dy[k]], [i, j], cnt+1, k)
                else:
                    escape([x, y], [i, j], cnt+1, k)
            else:
                continue

n, m = map(int, stdin.readline().split())
maps =list(list(stdin.readline().rstrip()) for _ in range(n))
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'R':
            red = [i, j]
        if maps[i][j] == 'B':
            blue = [i, j]
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1) # 하 상 우 좌

escape(red, blue, 0, 10)
print(0)