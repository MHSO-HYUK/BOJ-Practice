# 16932 모양 만들기
from sys import stdin
from collections import deque
def cluster(i, j):
    global num
    queue = deque([[i, j]])
    visit[i][j] = num
    cnt = 0
    while(queue):
        x, y  = queue.popleft()
        cnt += 1
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx <=n-1 and 0 <= ny <= m-1:
                if maps[nx][ny] and not visit[nx][ny]:
                    visit[nx][ny] = num
                    queue.append([nx, ny])

    temp.append(cnt)
    
n, m = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split()))for _ in range(n))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visit = [[0]*m for _ in range(n)]
temp = [0]
num = 1
for i in range(n):
    for j in range(m):
        if maps[i][j] and not visit[i][j]:
            cluster(i, j)
            num+=1

maxima = max(temp) + 1
for i in range(n):
    for j in range(m):
        if not maps[i][j]:
            cache = []
            for k in range(4):
                x, y = i+dx[k], j+dy[k]
                if 0 <= x <= n-1 and 0 <= y <= m-1:
                    if maps[x][y]:
                        flag = False
                        for a, b in cache:
                            if visit[a][b] == visit[x][y]:
                                flag = True
                        if not flag:
                            cache.append([x, y])
                            
            if len(cache) >= 2:
                sums = 0
                for a in range(len(cache)):
                    sums += temp[visit[cache[a][0]][cache[a][1]]]
                maxima = max(maxima, sums+1)
print(maxima)