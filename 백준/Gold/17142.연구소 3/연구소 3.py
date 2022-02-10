# 17142 연구소 3
from sys import stdin
from collections import deque
from itertools import combinations
def virus():
    queue = deque()
    num = 0
    for i in range(n):
        for j in range(n):
            if(maps[i][j] == 3):
                queue.append([i, j, 0])
            if(maps[i][j] == 0):
                num += 1
                
    visit = [[0 for _ in range(n)] for _ in range(n)]
    if(num == 0):
        return num
    
    while(queue and num != 0):
        x, y, cnt =queue.popleft()
        for k in range(4):
            a, b= x+dx[k], y+dy[k]
            if 0<=a<=n-1 and 0<=b<=n-1:
                if(maps[a][b] == 0 and visit[a][b] == 0):
                    visit[a][b] = 1
                    num -= 1
                    queue.append([a, b, cnt+1])
                    
                if maps[a][b] == 2 and visit[a][b] == 0:
                    visit[a][b] = 1
                    queue.append([a, b, cnt+1])
                    
    for i in range(n):
        for j in range(n):
            if (maps[i][j] == 0 and visit[i][j] == 0):
                return 10**10   

    return cnt+1

n, m = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
vir = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        if(maps[i][j] == 2):
            vir.append([i, j])

ans = 10**10
for a in combinations(vir, m):
    for v in a:
        maps[v[0]][v[1]] = 3
    ans = min(ans, virus())
    for v in a:
        maps[v[0]][v[1]] = 2

if(ans == 10**10):
    print(-1)
else:
    print(ans)