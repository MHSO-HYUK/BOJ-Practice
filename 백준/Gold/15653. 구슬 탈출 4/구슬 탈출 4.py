# 15653 구슬 탈출 4
from sys import stdin
def dfs(red, blue, cnt, before):
    global minima
    if cnt > minima:
        return
    for k in range(4):
        x, y = red
        a, b = blue
        if k != before:
            red_move, blue_move = 0, 0
            rflag, bflag = False , False
            i, j = x, y
            while(1):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                    if maps[nx][ny] == '#':
                        break
                        
                    if maps[nx][ny] == '.':
                        i, j = nx, ny
                        red_move += 1
                        continue
                        
                    if maps[nx][ny] == 'O':
                        red_move += 1
                        rflag = True
                        break
            
            p, q = a, b
            while(1):
                nx, ny = p + dx[k], q + dy[k]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                    if maps[nx][ny] == '#':
                        break
                        
                    if maps[nx][ny] == '.':
                        p, q = nx, ny
                        blue_move += 1
                        continue
                        
                    if maps[nx][ny] == 'O':
                        blue_move += 1
                        bflag = True
                        break
            
            
            if rflag and (not bflag):
                minima = min(minima, cnt)
                continue
                
            elif (not rflag) and (not bflag):
                if [i, j] == [p, q]:
                    if red_move > blue_move:
                        if visit[i-dx[k]][j-dy[k]][p][q] > cnt+1:
                            visit[i-dx[k]][j-dy[k]][p][q] = cnt+1
                            dfs([i-dx[k], j-dy[k]], [p, q], cnt+1, k)
                        
                    else:
                        if visit[i][j][p-dx[k]][q-dy[k]] > cnt+1:
                            visit[i][j][p-dx[k]][q-dy[k]] = cnt+1
                            dfs([i, j], [p-dx[k], q-dy[k]], cnt+1, k)
                else:
                    if visit[i][j][p][q] > cnt+1:
                        visit[i][j][p][q] = cnt+1
                        dfs([i, j], [p, q], cnt+1, k)
            
            else: # 무효한 경우
                continue
                        
n, m = map(int, stdin.readline().split())
maps = list( list(stdin.readline().rstrip()) for _ in range(n))
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'B':
            maps[i][j] = '.'
            blue = [i, j]
        if maps[i][j] == 'R':
            maps[i][j] = '.'
            red = [i, j]
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
minima = 10**10
visit = [[[[n*m for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
visit[red[0]][red[1]][blue[0]][blue[1]] = 1
dfs(red, blue, 1, -1)
if minima != 10**10:
    print(minima)
else:
    print(-1)