# 17244 아맞다우산
# 챙길 물건은 최대 5개 
from sys import stdin
from collections import deque
from copy import deepcopy
def bfs():
    queue = deque()
    dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
    queue.append([start[0], start[1], [0, 0, 0, 0, 0], 0])
    visit = [[[10**10 for _ in range(32)] for _ in range(m)] for _ in range(n)]
    visit[start[0]][start[1]][0] = 0
    while(queue):
        x, y, pick, cnt = queue.popleft()
        if [x, y] == end and sum(pick) == num:
            return cnt
        
        for k in range(4):
            temp = deepcopy(pick)
            nx, ny = x+dx[k], y + dy[k]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if maps[nx][ny] == '.':
                    p = 2**4*temp[4] + 2**3*temp[3] + 2**2*temp[2] + 2*temp[1] + temp[0]
                    if visit[nx][ny][p] > cnt+1:
                        visit[nx][ny][p] = cnt+1
                        queue.append([nx, ny, temp, cnt+1])

                elif type(maps[nx][ny]) == int :
                    if not pick[maps[nx][ny]]: # 이번에 새로 챙긴 케이스
                        p = 2**4*temp[4] + 2**3*temp[3] + 2**2*temp[2] + 2*temp[1] + temp[0]
                        p += 2**maps[nx][ny]
                        if visit[nx][ny][p] > cnt+1:
                            visit[nx][ny][p] = cnt+1
                            temp[maps[nx][ny]] = 1
                            queue.append([nx, ny, temp, cnt+1])

                    else: # 원래 챙겼던 칸 
                        p = 2**4*temp[4] + 2**3*temp[3] + 2**2*temp[2] + 2*temp[1] + temp[0]
                        if visit[nx][ny][p] > cnt+1: 
                            visit[nx][ny][p] = cnt+1
                            queue.append([nx, ny, temp, cnt+1])

m, n = map(int, stdin.readline().split())
maps = []
num = 0
for i in range(n):
    temp = list(stdin.readline().rstrip())
    for j in range(m):
        if temp[j] == 'S':
            temp[j] = '.'
            start = [i, j]
        if temp[j] == 'E':
            temp[j] = '.'
            end = [i, j]
        if temp[j] == 'X':
            temp[j] = num
            num += 1
    maps.append(temp)
print(bfs())