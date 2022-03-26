# 16137 견우와 직녀
from sys import stdin
from collections import deque
def bfs():
    queue = deque()
    queue.append([0, 0, 0, 0, 0])
    visit = [[[10**10, 10**10] for _ in range(n)] for _ in range(n)]
    dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
    minima = 10**10
    while(queue):
        x, y, time, used, before = queue.popleft()
        if time > minima:
            continue
        if [x, y] == [n-1, n-1]:
            minima = min(minima, time)
            continue
        for k in range(4):
            nx, ny = x+dx[k], y+ dy[k]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if maps[nx][ny] == 1:
                    if visit[nx][ny][used] > time+1:
                        visit[nx][ny][used] = time+1
                        queue.append([nx, ny, time+1, used, 0])
                
                if not before:
                    if maps[nx][ny] > 1:
                        if not (time+1) % maps[nx][ny]:
                            if visit[nx][ny][used] > time+1:
                                visit[nx][ny][used] = time+1
                                queue.append([nx, ny, time+1, used, 1])
                        else:
                            temp = time + 1
                            while(temp % maps[nx][ny]):
                                temp += 1
                            if visit[nx][ny][used] > temp:
                                visit[nx][ny][used] =  temp
                                queue.append([nx, ny, temp, used, 1])

                    elif maps[nx][ny] == 0:
                        if not used:
                            if not (time+1)%p:
                                if visit[nx][ny][1] > time+1:
                                    visit[nx][ny][1] = time+1
                                    queue.append([nx, ny, time+1, 1, 1])
                            else:
                                temp = time + 1
                                while(temp % p):
                                    temp += 1
                                if visit[nx][ny][1] > temp :
                                    visit[nx][ny][1] =  temp
                                    queue.append([nx, ny, temp, 1, 1])
    
    return minima

n, p = map(int, stdin.readline().split()) # p분 주기인 오작교를 하나 더 놓을 수 있다. 
maps = []
for i in range(n):
    temp = list(map(int, stdin.readline().split()))
    for j in range(n):
        if temp[j] > 1:
            ojak = [i, j]
    maps.append(temp)
print(bfs())