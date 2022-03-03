# 21609 상어 중학교
# 검정 (-1) / 무지개 (0) / 일반 (1~m)
# 그룹에는 적어도 하나의 일반 블록 + 색이 모두 같아야
# 검은색은 없어야 하고 무지개는 얼마든지 
# 그룹은 2개 이상 

# 그룹 형성 (없으면 끝)
# 기준 블록은 무지개가 아닌 것 중에 행이 작거나 열이 작은거
# 크기 -> 무지개가 많은 그룹 -> 기준 블록 행 큰 거 -> 열 큰 거


# 터트림
# 중력
# 반시계 회전 
# 중력
from sys import stdin
import heapq
from collections import deque
def rotation(maps):
    n = len(maps)
    nmaps = []
    for j in range(n-1, -1, -1):
        temp = []
        for i in range(n):
            temp.append(maps[i][j])
        nmaps.append(temp)
    return nmaps


def gravity(maps): # 검은색을 제외하고 떨어짐
    n = len(maps)
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if maps[i][j] == -2: # 빈칸 발견 
                for k in range(i-1, -1, -1): # 그 위에 대하여 
                    if maps[k][j] == -1:
                        break
                        
                    elif maps[k][j] != -2:
                        p = k
                        while(1):
                            if p+1 <= n-1 and maps[p+1][j] == -2:
                                maps[p+1][j], maps[p][j] = maps[p][j], -2
                                p += 1
                            else:
                                break
    return maps

def group(x, y, maps, color):
    global temp
    global gvisit
    queue = deque([[x, y]])
    visit = [[0]*n for _ in range(n)]
    visit[x][y] = 1
    gvisit[x][y] = 1
    color_cnt = 0
    block_cnt = 1
    while(queue):
        i, j = queue.popleft()
        for k in range(4):
            a, b = i+dx[k], j+dy[k]
            if 0<=a<=n-1 and 0<=b <= n-1:
                if not visit[a][b]:
                    if maps[a][b] == color: # 같은 색상
                        visit[a][b] = 1
                        gvisit[a][b] = 1
                        block_cnt += 1
                        queue.append([a, b])
                    if maps[a][b] == 0: # 무지개
                        visit[a][b] = 1
                        color_cnt += 1
                        block_cnt += 1
                        queue.append([a, b])

    if block_cnt > 1:
        flag = False
        for i in range(n):
            if not flag:
                for j in range(n):
                    if visit[i][j] and maps[i][j] == color:
                        a, b= i, j
                        flag = True
                        break
        heapq.heappush(temp, [-block_cnt, -color_cnt, -a, -b])
                        
    
def bang(x, y, maps, color):
    score = 0
    queue = deque([[x, y]])
    visit = [[0]*n for _ in range(n)]
    visit[x][y] = 1
    while(queue):
        i, j = queue.popleft()
        for k in range(4):
            a, b = i+dx[k], j+dy[k]
            if 0<=a<=n-1 and 0<=b <= n-1:
                if not visit[a][b]:
                    if maps[a][b] == color: # 같은 색상
                        visit[a][b] = 1
                        queue.append([a, b])
                    if maps[a][b] == 0: # 무지개
                        visit[a][b] = 1
                        queue.append([a, b])
               
    for i in range(n):
        for j in range(n):
            if visit[i][j]:
                score += 1
                maps[i][j] = -2
    return maps, score**2


n, m = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
t = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
ans = 0
while(1):
    temp = []
    gvisit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if 1 <= maps[i][j] <= m and not gvisit[i][j]:
                group(i, j, maps, maps[i][j])
                
    if not temp:
        break

    a, b, c, d = heapq.heappop(temp)
    maps, t = bang(-c, -d, maps, maps[-c][-d])

    ans += t
    maps = gravity(maps)  

    maps = rotation(maps)

    maps = gravity(maps)

print(ans)