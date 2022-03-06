# 19237 어른 상어
from sys import stdin
import sys
import heapq
n, m, last = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
dir = [0] + list(map(int, stdin.readline().split())) # 각 상어의 방향
usun = [[] for _ in range(m+1)] # 각 상어의 방향 우선순위
for i in range(1, m+1):
    usun[i].append(0)
    for _ in range(4):
        usun[i].append(list(map(int, stdin.readline().split())))
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1] # 1, 2, 3, 4 = 위 아래 왼쪽 오른쪽
# 맨 처음 모든 상어가 자신의 위치에 냄새를 뿌림
smell = [[[] for _ in range(n)] for _ in range(n)] # [상어 번호, 남은 시간]
loc = [0 for _ in range(m+1)]
for i in range(n):
    for j in range(n):
        if maps[i][j]:
            smell[i][j] = [maps[i][j], last]
            loc[maps[i][j]] = [i, j]
cnt, time = 0, 0
while(1):
# 이동방향을 결정할 때는 냄새가 없는 칸의 방향으로 잡는다 // 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
# 가능한 칸이 여러 개라면 우선순위를 따짐 // 맨 처음을 제외하고는 보고 있는 방향은 이동한 방향이 된다.
# 모든 상어가 이동한 뒤, 한 칸에 여러 마리의 상어가 남아 있으면 가장 작은 번호를 가진 상어를 제외하고 죽음
# 1. 냄새가 없는 칸 // 2. 자신의 냄새가 있는 칸 // 3. 우선순위
    for i in range(1, m+1):
        if loc[i]: # 상어가 살아 있다면
            x, y = loc[i]
            temp = []
            for k in range(1, 5):
                a, b = x+dx[k], y+dy[k]
                if 0 <= a <= n-1 and 0 <= b <= n-1:
                    if not smell[a][b]: # 냄새가 없다면
                        p, q = 0, 0
                    else:
                        p = 1
                        if smell[a][b][0] == i: # 냄새가 내꺼라면
                            q = 0
                        else:
                            q = 1
                    # 우선순위 // 1 위 2 아래 3 왼쪽 4 오른쪽
                    for v in range(4):
                        if usun[i][dir[i]][v] == k:
                            t = v
                            break
                    heapq.heappush(temp, [p, q, t, a, b, k])
            p, q, t, a, b, k = heapq.heappop(temp)
            dir[i] = k # 다음번 바라보는 방향
            loc[i] = [a, b]

    for i in range(m, 0, -1):
        if loc[i]:
            smell[loc[i][0]][loc[i][1]] = [i, last+1]


    for i in range(n):
        for j in range(n):
            if smell[i][j]:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = []

    for i in range(1, m+1):
        for j in range(i+1, m+1):
            if loc[i] == loc[j] and loc[i] != 0:
                loc[j] = 0
                dir[j] = -1
                cnt += 1

    time += 1
    if cnt == m-1:
        break

    if time >= 1000:
        print(-1)
        sys.exit()

print(time)