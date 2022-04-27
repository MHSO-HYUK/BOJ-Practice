# 21609 상어 중학교
from sys import stdin
from collections import deque
import heapq
def gravity(new_maps):
    for i in range(n-1, -1, -1):
        for j in range(n):
            if new_maps[i][j] != -1 and new_maps[i][j] != -2: # 검정 혹은 빈칸이 아닌 경우
                x = i + 1
                while(1):
                    if x < n and new_maps[x][j] == -2: # 격자 내부이고 블록이 없는 경우
                        x += 1 # 하강 
                    else: # 바닥에 부딫히거나 블록이 있는 경우
                        break # 정지
                x -= 1
                new_maps[x][j], new_maps[i][j] = new_maps[i][j], new_maps[x][j]
    return new_maps

def rotate(new_maps):
    ret_maps = []
    for j in range(n-1, -1, -1):
        cache = []
        for i in range(n):
            cache.append(maps[i][j])
        ret_maps.append(cache)
    return ret_maps
    
    
def find_group(x, y):
    # 그룹에는 일반 블록이 하나 이상 있어야 하며 색이 모두 같아야 한다.
    # 검정 블록은 포함되면 안되고 무지개는 얼마든지 있어도 된다. 
    # 그룹의 블록은 2개 이상 
    # 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중 행의 번호, 열의 번호 작은 순
    # 1. 크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러개 라면 포함된 
    #무지개 블록수가 가장 많은 그룹 > 기준 블록의 행이 가장 큰 것 > 기준 블록의 열이 가장 큰 것
    queue = deque()
    rainbow, lr, lc = 0, x, y
    check = [[0 for _ in range(n)] for _ in range(n)]
    visit[x][y], check[x][y] = 1, 1
    color = maps[x][y]
    queue.append([x, y])
    cache = []
    cnt = 0
    while(queue):
        x, y = queue.popleft()
        cache.append([x, y])
        cnt += 1
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx <= n-1 and 0 <= ny  <= n-1:
                if not check[nx][ny]:
                    if maps[nx][ny] == 0: # 인접한 무지개 블록
                        check[nx][ny] = 1
                        rainbow += 1
                        queue.append([nx, ny])
                    elif maps[nx][ny] == color: # 인접한 동일 색깔 블록 
                        lr = min(lr, nx)
                        lc = min(lc, ny)
                        visit[nx][ny], check[nx][ny] = 1, 1
                        queue.append([nx, ny])
    
    return [-cnt, -rainbow, -lr, -lc, cache]
    
n, m = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
dx, dy = [1, -1, 0 ,0], [0, 0, 1, -1]
# 검정 -1 무지개 0 일반 1 ~ M // 빈칸 -2 로 정의! 
# 그룹에는 일반 블록이 하나 이상 있어야 하며 색이 모두 같아야 한다.
# 검정 블록은 포함되면 안되고 무지개는 얼마든지 있어도 된다. 
# 그룹의 블록은 2개 이상 
# 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중 행의 번호, 열의 번호 작은 순
score = 0
while(1):
    heap = []
    visit = [[0 for _ in range(n)] for _ in range(n)]
    # 1. 크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러개 라면 포함된 
    #무지개 블록수가 가장 많은 그룹 > 기준 블록의 행이 가장 큰 것 > 기준 블록의 열이 가장 큰 것
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and 1 <= maps[i][j]:
                cnt, rainbow, lr, lc, cache = find_group(i, j)
                if -cnt >= 2:
                    heapq.heappush(heap, [cnt, rainbow, lr, lc, cache])

    if heap:
        cnt, rainbow, lr, lc, cache = heapq.heappop(heap)
    else:
        break
# 2. 1에서 찾은 블록 그룹 제거 -> 블록수^2 획득
    for a, b in cache:
        maps[a][b] = -2
    score += cnt**2
# 3. 중력 작용
    maps = gravity(maps)
# 4. 90도 반시계 회전
    maps = rotate(maps)
# 5.  중력 작용
    maps = gravity(maps)
print(score)
