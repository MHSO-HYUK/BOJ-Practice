# 16236 아기 상어
# 처음 아기상어의 크기 = 2 // 상하좌우 이동
# 자기보다 큰 물고기가 있는 칸은 못 지나감
# 자기보다 작은 물고기를 먹을 수 있음 
# 먹을 수 있는 물고기가 하나면 그쪽으로 간다. 
# 먹을 수 있는 물고기가 하나 이상이면 칸이 최소 + 가장 왼쪽 
# 자신의 크기와 같은 수의 물고기를 먹으면 크기가 + 1이 된다.  
from sys import stdin
import heapq
from collections import deque
def mom(size, X, Y, cnt, time):
    global ans
    ans = max(time, ans)
    if(size == cnt):
        size , cnt = size+1, 0  
    queue = deque([[X, Y]]) # 상어의 현재 위치 
    dist = [[0 for _ in range(n)] for _ in range(n)]
    
    while(queue): # 먹이 거리 계산 큐
        x, y = queue.popleft()
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if(0<=a<=n-1 and 0<=b<=n-1 and not (a == X and b == Y)):
                if(maps[a][b] <= size and dist[a][b] == 0): # 상어가 지나다닐 수 있는 길 
                    dist[a][b] = dist[x][y] + 1
                    queue.append([a, b])
    can = []
    for a in range(n):
        for b in range(n):
            if(0 < maps[a][b] < size and visit[a][b] == 0 and dist[a][b]): # 동시에 상어가 먹을 수 있는 곳 탐색 
                heapq.heappush(can, [dist[a][b], a, b]) # 거리 최소 -> y좌표 최소
    if(can):
        dt, nx, ny = heapq.heappop(can)
        visit[nx][ny] = 1
        mom(size, nx, ny, cnt+1, time+dt)
        
    return ans   

n = int(stdin.readline())
maps = []
for _ in range(n):
    maps.append(list(map(int, stdin.readline().split())))
fish = []
for i in range(n):
    for j in range(n):
        if(maps[i][j] == 9):
            shark = [2, i, j, 0, 0] 
            maps[i][j] = 0
            
dx, dy = [1, -1, 0 , 0], [0, 0, 1, -1]
ans = 0
visit = [[0 for _ in range(n)] for _ in range(n)]
print(mom(shark[0], shark[1], shark[2], shark[3], shark[4]))