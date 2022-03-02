# 14500 테트로미노
# 정사각형 4개를 이어 붙힌 도형
from sys import stdin

def tetro(a, b, cnt, val, d1, d2):
    global temp
    if cnt == 4:
        temp = max(temp, val)
        return
    else:
        for k in range(4):
            x, y = a+dx[k], b+dy[k]
            if 0 <= x <= n-1 and 0 <= y <= m-1:
                if not visit[x][y]:
                    visit[x][y] = 1
                    tetro(x, y, cnt+1, val+maps[x][y], k, d1)
                    visit[x][y] = 0

        if cnt == 3 and d1 == d2: # 3회 이동 + 같은 방향 두번 이동 시
            for k in [1, 3]:
                p, q = a-dx[d1]+dx[d1-k], b-dy[d2]+dy[d2-k]
                if 0 <= p <= n-1 and 0 <= q <= m-1:
                    temp = max(temp, val + maps[p][q])


    return temp

dx, dy = (1,0,-1,0),(0,1,0,-1)
n, m =map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
maxima = 0
visit = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        temp = 0
        visit[i][j] = 1
        maxima = max(maxima, tetro(i, j, 1, maps[i][j], -1, -1))
visit = [[0]*m for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(m):
        temp = 0
        visit[i][j] = 1
        maxima = max(maxima, tetro(i, j, 1, maps[i][j], -1, -1))

print(maxima)