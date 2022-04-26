# 13460 구슬 탈출 2
# 빨간 색만 넣고 파란 색은 안 넣은 방향으로 
from sys import stdin
dx, dy = [1, -1, 0 , 0], [0, 0, 1, -1]
def escape(red, blue, cnt, before):
    global minima 
    #네 방향 중 하나로 기울인다. 
    if cnt >= minima or cnt > 10: # 최소 이동 횟수보다 크거나 같은 경우에는 멈춘다
        return
    
    for k in range(4):
        rflag, bflag = False, False # 들어갔는지 여부를 체크하는 플레그
        rmove, bmove = 0, 0 # 이동 거리를 체크하는 플레그
        x, y = red
        a, b = blue
        if k != before: # 똑같은 방향으로 두번 연속 기울이는 것은 의미가 없음
            while(1):
                nx, ny = x+dx[k], y+dy[k]
                if maps[nx][ny] == '#': # 구슬이 벽에 부딫히면 이동 종료
                    break
                rmove += 1
                if maps[nx][ny] == 'O': # 구슬이 구멍에 빠지면 이동 종료
                    rflag = True
                    break
                else:
                    x, y = nx, ny # 둘다 아니라면 한번 더 이동하기
                
            while(1):
                na, nb = a+dx[k], b+dy[k]
                if maps[na][nb] == '#': # 구슬이 벽에 부딫히면 이동 종료
                    break
                bmove += 1
                if maps[na][nb] == 'O': # 구슬이 구멍에 빠지면 이동 종료
                    bflag = True
                    break
                else:
                    a, b = na, nb # 둘다 아니라면 한번 더 이동하기

            if rflag and not bflag: # 종료 조건 만족시
                minima = min(minima, cnt)

            elif not rflag and not bflag: # 종료 조건 만족 X 시
                if [x, y] == [a, b]: # 두 구슬이 겹친 경우
                    if rmove < bmove: # 더 많이 이동한 구슬이 늦게 온 것 
                        a, b = a-dx[k], b-dy[k]
                    else:
                        x, y = x-dx[k], y-dy[k]
                    if visit[x][y][a][b] > cnt:
                        visit[x][y][a][b] = cnt
                        escape([x, y], [a, b], cnt+1, k)
                else:
                    if visit[x][y][a][b] > cnt:
                        visit[x][y][a][b] = cnt
                        escape([x, y], [a, b], cnt+1, k)
            else:
                continue

n, m = map(int, stdin.readline().split())
maps = []
for i in range(n):
    temp = list(stdin.readline().rstrip())
    for j in range(m):
        if temp[j] == 'R':
            red = [i, j]
            temp[j] = '.'
        if temp[j] == 'B':
            blue = [i, j]
            temp[j] = '.'
    maps.append(temp)
    
minima = 10**10
visit = [[[[10**10 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
x, y = red
a, b = blue
visit[x][y][a][b] = 0
escape(red, blue, 1, -1)
if minima > 10:
    print(-1)
else:
    print(minima)