# 16988 Baaaaaaaaaaaaaaaaaaaduk2(Easy)
from sys import stdin
from collections import deque, defaultdict
import heapq
dx, dy = (1, -1, 0 ,0), (0, 0, 1, -1)
def cluster(i, j):
    check = [[0]*m for _ in range(n)]
    check[i][j] = 1
    queue = deque([[i, j]])
    while(queue): # 1. 흰돌 클러스터를 찾아본다. 
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if not visit[nx][ny] and maps[nx][ny] == 2:
                    visit[nx][ny], check[nx][ny] = 1, 1
                    queue.append([nx, ny])
    
    
    #2. 해당 클러스트를 에워싸기 위해 필요한 검은 돌의 숫자를 찾아본다. 
    for i in range(n):
        for j in range(m):
            if check[i][j] == 1:
                for k in range(4):
                    x, y = i + dx[k], j+dy[k]
                    if 0 <= x <= n-1 and 0 <= y <= m-1:
                        if maps[x][y] == 0:
                            check[x][y] = 2

    num, black = 0, 0
    cache = []
    for i in range(n):
        for j in range(m):
            if check[i][j] == 1:
                num += 1
            if check[i][j] == 2:
                black += 1
                cache.append((i, j))
    

    return [black, -num, cache]
    

n, m = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
# 자신의 돌로 상대방의 그룹을 빈틈없이 에워싸도록
# 흰돌 그릅 내에 빈칸과 인접한 돌이 없다
visit = [[0]*m for _ in range(n)]
need = []
for i in range(n):
    for j in range(m):
        if not visit[i][j] and maps[i][j] == 2:
            visit[i][j] = 1
            a, b, c = cluster(i, j)
            if a <= 2:
                need.append((a, b, c))
final = []
need.sort(key = lambda x : x[2])
loc = defaultdict(list)
for i in range(len(need)):
    if not tuple(need[i][2]) in loc:
        loc[tuple(need[i][2])] = -need[i][1]
    else:
        loc[tuple(need[i][2])] -= need[i][1]
cache = []
for i in range(len(need)):
    if need[i][0] == 1:
        cache.append(need[i])

for i in cache:
    for k in loc:
        if i[2][0] in k and len(k) > 1:
            loc[k] -= i[1]
maxima = 0
for k in loc:
    maxima = max(maxima, loc[k])
one = []
for k in loc:
    if len(k) == 1:
        heapq.heappush(one, (-loc[k]))
if len(one) > 1:
    a, b = heapq.heappop(one), heapq.heappop(one)
    maxima = max(maxima, -a-b)
print(maxima)