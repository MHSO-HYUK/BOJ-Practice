#17141 연구소 2
# 0/빈칸 1/벽 2/ 바이러스 놓을 수 있는 칸
from sys import stdin
import itertools
from collections import deque
def virus():
    global n
    dx, dy = [1, -1, 0 ,0], [0, 0, 1, -1]
    flag = False
    while(queue):
        x, y, c = queue.popleft()
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if 0<= a <= n-1 and 0<= b <= n-1:
                if(visit[a][b] == 0 and (maps[a][b] == 0 or maps[a][b] == 2)):
                    visit[a][b] = 1
                    queue.append([a,b,c+1])
                    
    for i in range(n):
        for j in range(n):
            if(visit[i][j] == 0 and (maps[i][j] == 0 or maps[i][j] == 2)):
                return 10**15
            
    return c


n, m = map(int, stdin.readline().split()) # m : 바이러스를 놓을 수 있는 갯수
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
ill = [] # 바이러스를 놓을 수 있는 공간 좌표 모음 
for i in range(n):
    for j in range(n):
        if(maps[i][j] == 2):
            ill.append([i,j, 0])
           
minima = 10**15
for com in list(itertools.combinations(ill, m)):
    queue = deque()
    visit = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        queue.append(com[i])
        visit[com[i][0]][com[i][1]] = 1
    minima = min(minima, virus())
 
if(minima == 10**15):
    print(-1)
else:
    print(minima)