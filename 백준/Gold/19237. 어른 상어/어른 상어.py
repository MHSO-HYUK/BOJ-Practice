# 19237 어른 상어
from sys import stdin
import heapq
n, m, last = map(int, stdin.readline().split())
maps = [[[] for _ in range(n)] for _ in range(n)] # 상어 지도
info = [[] for _ in range(m)] # 상어 이동 정보
sloc = [[] for _ in range(m)] # 상어 위치
for i in range(n):
    temp = list(map(int, stdin.readline().split()))
    for j in range(n):
        if temp[j]:
            maps[i][j].append(temp[j]-1)
            sloc[temp[j]-1]= [i, j]

sd = list(map(int, stdin.readline().split()))
for i in range(m):
    sd[i] -= 1
alive = [1 for _ in range(m)] # 살아 있는지 여부
smell = [[[] for _ in range(n)] for _ in range(n)] # 냄새 지도
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(m):
    for j in range(4):
        a, b, c, d = map(int, stdin.readline().split())
        info[i].append([a-1, b-1, c-1, d-1])
time = 0
while(1):
    # 모든 상어가 자신의 위치에 냄새를 뿌린다.
    time += 1
    for i in range(m):
        if alive[i]:
            smell[sloc[i][0]][sloc[i][1]] = [last, i]
    # 1초마다 모든 상어가 동시에 상하좌우중 인접한 칸 하나로 이동(냄새는 k번 이동하고 나면 사라진다.)
    # 인접한 칸중 냄새가 없는 칸 > 그런 칸이 없다면 자신의 냄새가 있는 칸
    # 그런 칸이 여러개라면 특정 우선순위에 따라 다르다 . 
    maps = [[[] for _ in range(n)] for _ in range(n)] # 상어 지도
    for idx in range(m):
        if alive[idx]: #살아 있다면?
            x, y = sloc[idx]
            heap = []
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                    if not smell[nx][ny]: # 냄새가 없는 칸?
                        heapq.heappush(heap, [0, info[idx][sd[idx]].index(k), nx, ny, k])
                    else:
                        if smell[nx][ny][1] == idx: # 자신의 냄새가 있는 칸
                            heapq.heappush(heap, [1, info[idx][sd[idx]].index(k),nx, ny, k])
                            
            s, i, x, y, dirc = heapq.heappop(heap)
            sloc[idx] = [x, y] # 이동
            sd[idx] = dirc
            maps[x][y].append(idx)
            
    # 이동한 뒤 한 칸에 여러 상어가 있다면 가장 작은 번호 상어를 제외하고 모두 나가리 
    for i in range(n):
        for j in range(n):
            if smell[i][j]:
                smell[i][j][0] -= 1
                if smell[i][j][0] == 0:
                    smell[i][j] = []
                    
            if len(maps[i][j]) >= 2: # 두마리 이상의 상어
                for z in range(1, len(maps[i][j])):
                    alive[maps[i][j][z]] = 0
                
    if sum(alive) == 1:
        break
    if time > 1000:
        break
if time > 1000:
    print(-1)
else:
    print(time)