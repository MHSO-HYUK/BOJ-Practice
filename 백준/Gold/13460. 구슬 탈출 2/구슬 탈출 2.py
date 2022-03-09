# 13460 구슬 탈출 2
from sys import stdin
import sys
sys.setrecursionlimit(10**5)
def move(cnt, red, blue, before):
    global ans
    if cnt > 9 or cnt > ans: #답보다 낮은 케이스는 그냥 없어져도 됌
        return

    for k in range(4):
        if k != before: # 두번 연속 같은 방향으로 기울이지 못하도록 (의미 없음)
            s = True
            x, y = red
            p, q = blue
            if k == 0: # 하
                if y == q: # y 좌표가 같다면 -> 밑으로 떨어질 때 원래 밑에 있던게 더 먼저 도착
                    s = True if x > p else False # R가 B보다 앞에 있으면 True
            elif k == 1: # 상
                if y == q:
                    s = True if x < p else False
            elif k == 2: # 우
                if x == p: # x 좌표가 같다면 -> 원래 오른쪽에 있던 게 더 먼저 도착
                    s = True if y > q else False
            elif k == 3: # 좌
                if x == p:
                    s = True if y < q else False

            rflag, bflag = False, False
            while(1): # 빨간 구슬의 이동
                rx, ry = x + dx[k], y + dy[k]
                if maps[rx][ry] == '#':
                    break
                if maps[rx][ry] == 'O':
                    rflag = True
                    break
                else:
                    x, y = rx, ry

            while(1): # 파란 구슬의 이동
                bx, by = p + dx[k], q + dy[k]
                if maps[bx][by] == '#':
                    break
                if maps[bx][by] == 'O':
                    bflag = True
                    break
                else:
                    p, q = bx, by


            if rflag and not bflag: # 정상적인 종료 케이스
                ans = min(ans, cnt+1)
                continue

            elif (rflag and bflag) or (not rflag and bflag): #에러가 난 케이스
                continue

            else:
                if [x, y] == [p, q]: # 겹쳐 버림
                    if s: # R이 먼저 도착
                        move(cnt+1, [x, y], [p - dx[k], q - dy[k]], k)
                    else:
                        move(cnt+1, [x - dx[k], y - dy[k]], [p, q], k)

                else:
                    move(cnt+1, [x, y], [p, q], k)


n, m = map(int, stdin.readline().split())
maps = list(list(stdin.readline().rstrip()) for _ in range(n))
dx, dy = [1, -1, 0 ,0], [0, 0, 1, -1]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'R':
            red = [i, j]
        if maps[i][j] == 'B':
            blue = [i, j]



ans = 10**10
move(0, red, blue, 10)
if ans == 10**10:
    print(-1)
else:
    print(ans)