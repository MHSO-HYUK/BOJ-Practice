# 21609 상어 중학교
from sys import stdin
from collections import deque
import heapq
def group(i, j, color):
    # 1. 크기가 가장 큰 블록 그룹을 찾는다. > 무지개 많은 것 > 기준 블록의 행이 큰것 > 열이 큰 것
    # 기준 블록 // 무지개가 아닌것 중 행의 번호 작은 것 > 열의 번호 작은 것
    # 0 무지개 -1 검정 1 ~ m 색깔
    queue = deque()
    queue.append([i, j])
    check = [[0 for _ in range(n)] for _ in range(n)]
    check[i][j] = 1
    cnt = 0
    rainbow = 0
    minr, minc = i, j
    cache = []
    while(queue):
        cnt += 1
        x, y = queue.popleft()
        cache.append([x, y])
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if not check[nx][ny]:
                    if maps[nx][ny] == color: # 동일 색깔
                        visit[nx][ny], check[nx][ny] = 1, 1
                        minr = min(minr, nx)
                        if minr == nx:
                            minc = min(minc, ny)
                        queue.append([nx, ny])
                    if maps[nx][ny] == 0: #무지개
                        rainbow += 1
                        check[nx][ny] = 1
                        queue.append([nx, ny])
    if cnt >= 2:
        return [-cnt, -rainbow, -minr, -minc, cache]
    else:
        return None

def gravity(new_maps):
    for j in range(n):
        for i in range(n-1 ,-1, -1):
            if 0 <= new_maps[i][j]:
                x, y = i, j
                while(1):
                    nx, ny = x + 1, y
                    if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                        if new_maps[nx][ny] == -2:
                            new_maps[x][y], new_maps[nx][ny] = new_maps[nx][ny], new_maps[x][y]
                            x, y = nx, ny
                            continue
                        else:
                            break
                    else:
                        break
    return new_maps

def rotate(new_maps):
    ret = []
    for j in range(n-1, -1, -1):
        temp = []
        for i in range(n):
            temp.append(new_maps[i][j])
        ret.append(temp)
    return ret

n, m = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
score = 0
while(1):
    # 1. 크기가 가장 큰 블록 그룹을 찾는다. > 무지개 많은 것 > 기준 블록의 행이 큰것 > 열이 큰 것
    # 기준 블록 // 무지개가 아닌것 중 행의 번호 작은 것 > 열의 번호 작은 것
    # 0 무지개 -1 검정 1 ~ m 색깔
    visit = [[0 for _ in range(n)] for _ in range(n)]
    heap = []
    for i in range(n):
        for j in range(n):
            if 1 <= maps[i][j] and not visit[i][j]:
                visit[i][j] = 1
                temp = group(i, j, maps[i][j])
                if temp:
                    heapq.heappush(heap, temp)
    if heap:
        cnt, rain, x, y, cache = heapq.heappop(heap)
    else:
        break
    # 2. 블록 그룹의 블록을 제거 한다 이때 제곱점수 획득 (그룹 없으먄 종료)
    for x, y in cache:
        maps[x][y] = -2 # 빈칸으로 만듬
    score += cnt**2

    # 3. 중력
    maps = gravity(maps)
    # 4. 90도 반시계
    maps = rotate(maps)
    # 5. 중력
    maps = gravity(maps)

print(score)