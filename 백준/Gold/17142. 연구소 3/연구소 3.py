# 17142 연구소 3
from sys import stdin
from itertools import combinations 
from collections import deque
def dfs(v):
    global total
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque()
    for x, y in v:
        queue.append([x, y, 0])
        visit[x][y] = 1    
    fill = 0
    while(queue):
        x, y, cnt = queue.popleft()
        if not maps[x][y]:
            fill += 1
        if fill == total:
            return cnt
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if not visit[nx][ny] and maps[nx][ny] != 1:
                    visit[nx][ny] = 1
                    queue.append([nx, ny, cnt+1])
    
    
    if fill == total: # 모든 칸을 꽉 채웠다면
        return cnt
    else:
        return 10**10

n, m = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
# 모든 빈칸에 바이러스를 퍼뜨리는 최소 시간을 구하자
lineup = []
total = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            lineup.append([i, j])
        if maps[i][j] == 0:
            total += 1

minima = 10**10
for v in combinations(lineup, m):
    minima = min(minima, dfs(v))

if minima == 10**10:
    print(-1)
else:
    print(minima)