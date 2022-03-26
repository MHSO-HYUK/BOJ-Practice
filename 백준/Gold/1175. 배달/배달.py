# 1175 배달
# 매 시간 방향을 바꿔야 한다. 
from sys import stdin
from collections import deque
def bfs():
    queue = deque()
    queue.append([start[0], start[1], 0, 0, 0, -1])
    dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
    visit = [[[[10**10, 10**10, 10**10, 10**10] for _ in range(4)]for _ in range(m)] for _ in range(n)]
    while(queue):
        x, y, a, b, now, bef = queue.popleft()
        if a == 1 and b == 1:
            return now
        for k in range(4):
            if k != bef:
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                    if maps[nx][ny] == '.':
                        if visit[nx][ny][k][2*a+b] > now+1:
                            visit[nx][ny][k][2*a+b] = now+1
                            queue.append([nx, ny, a, b, now+1, k])
                    if type(maps[nx][ny]) == int:
                        if maps[nx][ny] == 0:
                            if visit[nx][ny][k][2+b] > now+1:
                                visit[nx][ny][k][2+b] = now+1
                                queue.append([nx, ny, 1, b, now+1, k])
                        else:
                            if visit[nx][ny][k][2*a+1] > now+1:
                                visit[nx][ny][k][2*a+1] = now+1
                                queue.append([nx, ny, a, 1, now+1, k])
    return -1

n, m = map(int, stdin.readline().split())
maps = []
start = []
num = 0
for i in range(n):
    temp = list(stdin.readline().rstrip())
    for j in range(m):
        if temp[j] == 'S':
            start = [i, j]
            temp[j] = '.'
        if temp[j] == 'C':
            temp[j] = num
            num += 1
    maps.append(temp)
print(bfs())