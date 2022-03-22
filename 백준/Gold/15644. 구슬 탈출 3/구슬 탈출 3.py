# 15644 구슬 탈출 3
from sys import stdin
import sys
sys.setrecursionlimit(10**5)
def bizz(red, blue, cnt, log, bef):
    global minima, temp
    if cnt >= minima  or cnt > 10:
        return
    for k in range(4):
        if k == bef:
            continue
        x, y = red
        a, b = blue
        rm, bm = 0, 0
        rf, bf = False, False
        while(1):
            nx, ny = x +dx[k], y+dy[k]
            if maps[nx][ny] == 'O':
                rf = True
                break
            elif maps[nx][ny] != '#':
                x, y = nx, ny
                rm += 1
            else:
                break
        while(1):
            na, nb = a+dx[k], b+dy[k]
            if maps[na][nb] == 'O':
                bf = True
                break
            elif maps[na][nb] != '#':
                a, b = na, nb
                bm += 1
            else:
                break
    
        if rf and not bf: # 빨강이만 들어감
            minima = min(minima, cnt+1)
            if minima == cnt+1:
                temp = log+[k]
        
        
        elif not rf and not bf: # 둘다 안들어감
            if [x, y] == [a, b]: # 겹쳐버림
                if rm < bm:
                    a, b = a-dx[k], b-dy[k]
                    bizz([x, y], [a, b], cnt+1, log+[k], k)

                else:
                    x, y = x-dx[k], y-dy[k]
                    bizz([x, y], [a, b], cnt+1, log+[k], k)
     
            else: # 안겹침
                bizz([x, y], [a, b], cnt+1, log+[k], k)

        
n, m = map(int, stdin.readline().split())
maps = list(list(stdin.readline().rstrip()) for _ in range(n))
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'R':
            red = [i, j]
        if maps[i][j] == 'B':
            blue = [i, j]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
temp, minima = 0, 10**10
bizz(red, blue, 0, [], 4)
if minima > 10:
    print(-1)
else:
    print(minima)
    for i in range(len(temp)):
        if temp[i] == 0:
            print('D', end ='')
        if temp[i] == 1:
            print('U', end ='')
        if temp[i] == 2:
            print('R', end ='')
        if temp[i] == 3:
            print('L', end ='')