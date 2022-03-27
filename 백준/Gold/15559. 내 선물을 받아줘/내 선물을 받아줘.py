# 15559 내선물을 받아줘
from sys import stdin
from collections import deque
def first(i, j):
    queue = deque([[i, j]])
    check = []
    check.append([i, j])
    while(queue):
        x, y = queue.popleft()
        nx, ny = x + dirc[maps[x][y]][0], y + dirc[maps[x][y]][1]
        if not [nx, ny] in check and not visit[nx][ny]: # 처음 방문
            check.append([nx, ny])
            queue.append([nx, ny])
            
        elif not [nx, ny] in check and visit[nx][ny]: # 다른 클러스터에 포함
            for a, b in check:
                visit[a][b] = 1
            return 0
        
        elif [nx, ny] in check: # 새로운 클러스터의 형성
            for a, b in check:
                visit[a][b] = 1
            return 1

n, m = map(int, stdin.readline().split())
maps = list(list(stdin.readline().rstrip()) for _ in range(n))
dirc = {'N': (-1, 0), 'W': (0, -1), 'E' : (0, 1), 'S' : (1, 0)}
visit = [[0 for _ in range(m)] for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            ans += first(i, j)
print(ans)