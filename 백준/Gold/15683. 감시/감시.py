# 15683 감시
from sys import stdin
from itertools import product
from copy import deepcopy
n, m =map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
# 0 // 빈칸  6 // 벽  1~5 // CCTV (8개를 넘지 않는다)
# 1 // 한방향 2 // 양방향 3 // 수직 양방향 4 // 세방향 5 // 네방향
# 사각지대의 최소 크기를 구하는 프로그램을 작성하자
cctv = []
five = []
num = 0
for i in range(n):
    for j in range(m):
        if 1 <= maps[i][j] <= 4:
            cctv.append([i, j, maps[i][j]])
            num += 1

        if maps[i][j] == 5:
            five.append([i, j])

dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
visit = [[0]*m for _ in range(n)]
for i in five:
    for k in range(4):
        x, y = i[0], i[1]
        while(1):
            a, b = x + dx[k], y + dy[k]
            if 0 <= a <= n-1 and 0 <= b <= m-1:
                if maps[a][b] == 6:
                    break
                else:
                    visit[a][b] = 1
                    x, y = a, b
            else:
                break

ans = 10**10
for d in product(range(4), repeat = num):
    n_visit = deepcopy(visit)
    for p in range(len(cctv)):
        if cctv[p][2] == 1: # 한방향
            x, y = cctv[p][0], cctv[p][1]
            while(1):
                a, b = x + dx[d[p]], y+dy[d[p]]
                if 0 <= a <= n - 1 and 0 <= b <= m - 1:
                    if maps[a][b] == 6:
                        break
                    else:
                        n_visit[a][b] = 1
                        x, y = a, b
                else:
                    break

        elif cctv[p][2] == 2: # 양방향
            x, y = cctv[p][0], cctv[p][1]
            while (1):
                a, b = x + dx[d[p]], y+dy[d[p]]
                if 0 <= a <= n - 1 and 0 <= b <= m - 1:
                    if maps[a][b] == 6:
                        break
                    else:
                        n_visit[a][b] = 1
                        x, y = a, b
                else:
                    break

            x, y = cctv[p][0], cctv[p][1]
            while (1):
                a, b = x + dx[d[p]-2], y+dy[d[p]-2]
                if 0 <= a <= n - 1 and 0 <= b <= m - 1:
                    if maps[a][b] == 6:
                        break
                    else:
                        n_visit[a][b] = 1
                        x, y = a, b
                else:
                    break

        elif cctv[p][2] == 3: # 수직 양방향
            x, y = cctv[p][0], cctv[p][1]
            while (1):
                a, b = x + dx[d[p]], y+dy[d[p]]
                if 0 <= a <= n - 1 and 0 <= b <= m - 1:
                    if maps[a][b] == 6:
                        break
                    else:
                        n_visit[a][b] = 1
                        x, y = a, b
                else:
                    break

            x, y = cctv[p][0], cctv[p][1]
            while (1):
                a, b = x + dx[d[p]-1], y+dy[d[p]-1]
                if 0 <= a <= n - 1 and 0 <= b <= m - 1:
                    if maps[a][b] == 6:
                        break
                    else:
                        n_visit[a][b] = 1
                        x, y = a, b
                else:
                    break


        elif cctv[p][2] == 4:
            x, y = cctv[p][0], cctv[p][1]
            while (1):
                a, b = x + dx[d[p]], y + dy[d[p]]
                if 0 <= a <= n - 1 and 0 <= b <= m - 1:
                    if maps[a][b] == 6:
                        break
                    else:
                        n_visit[a][b] = 1
                        x, y = a, b
                else:
                    break

            x, y = cctv[p][0], cctv[p][1]
            while (1):
                a, b = x + dx[d[p]-1], y + dy[d[p]-1]
                if 0 <= a <= n - 1 and 0 <= b <= m - 1:
                    if maps[a][b] == 6:
                        break
                    else:
                        n_visit[a][b] = 1
                        x, y = a, b
                else:
                    break

            x, y = cctv[p][0], cctv[p][1]
            while (1):
                a, b = x + dx[d[p]-2], y + dy[d[p]-2]
                if 0 <= a <= n - 1 and 0 <= b <= m - 1:
                    if maps[a][b] == 6:
                        break
                    else:
                        n_visit[a][b] = 1
                        x, y = a, b
                else:
                    break

    cnt = 0
    for i in range(n):
        for j in range(m):
            if not maps[i][j] and not n_visit[i][j]:
                cnt += 1


    ans = min(ans, cnt)

print(ans)
