# 12100 2048 (easy)
# 최대 다섯번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램 
from sys import stdin
from copy import deepcopy
dx, dy= [1, -1, 0, 0], [0, 0, 1, -1] # 아래 위 오른 왼
def move(maps, d): # 이동 함수
    if d == 0: # 아래
        for i in range(n-1, -1, -1): # 아래줄부터 탐색
            for j in range(n):
                if maps[i][j]:
                    a, b = i, j
                    while(1):
                        ni, nj = a + dx[d], b+dy[d]
                        if 0 <= ni <= n-1 and 0 <= nj <= n-1:
                            if not maps[ni][nj]:
                                maps[ni][nj], maps[a][b] = maps[a][b], maps[ni][nj]
                                a, b = ni, nj
                            else:
                                break
                        else:
                            break
                    
    elif d == 1: # 위
        for i in range(n): # 위부터 탐색
            for j in range(n):
                if maps[i][j]:
                    a, b = i, j
                    while(1):
                        ni, nj = a + dx[d], b+dy[d]
                        if 0 <= ni <= n-1 and 0 <= nj <= n-1:
                            if not maps[ni][nj]:
                                maps[ni][nj], maps[a][b] = maps[a][b], maps[ni][nj]
                                a, b = ni, nj
                            else:
                                break
                        else:
                            break
                    
    elif d == 2: # 우
        for j in range(n-1, -1, -1): # 우부터 탐색
            for i in range(n):
                if maps[i][j]:
                    a, b = i, j
                    while(1):
                        ni, nj = a + dx[d], b+dy[d]
                        if 0 <= ni <= n-1 and 0 <= nj <= n-1:
                            if not maps[ni][nj]:
                                maps[ni][nj], maps[a][b] = maps[a][b], maps[ni][nj]
                                a, b = ni, nj
                            else:
                                break
                        else:
                            break
                    
    elif d == 3: # 좌
        for j in range(n): # 좌부터 탐색
            for i in range(n):
                if maps[i][j]:
                    a, b = i, j
                    while(1):
                        ni, nj = a + dx[d], b+dy[d]
                        if 0 <= ni <= n-1 and 0 <= nj <= n-1:
                            if not maps[ni][nj]: # 빈칸인 경우
                                maps[ni][nj], maps[a][b] = maps[a][b], maps[ni][nj]
                                a, b = ni, nj
                            else:
                                break
                        else:
                            break
    return maps
    
def plus(maps, d): # 결합 함수
    if d == 0: # 아래
        for i in range(n-1, 0, -1): # 아래부터 탐색
            for j in range(n):
                if maps[i][j] and maps[i][j] == maps[i-1][j]: # 동일?
                    maps[i][j] += maps[i][j]
                    maps[i-1][j] = 0
                    
    elif d == 1: # 위
        for i in range(n-1): # 위부터 탐색
            for j in range(n):
                if maps[i][j] and maps[i][j] == maps[i+1][j]: # 동일?
                    maps[i][j] += maps[i][j]
                    maps[i+1][j] = 0
                    
    elif d == 2: # 우
        for j in range(n-1, 0, -1): # 우부터 탐색
            for i in range(n):
                if maps[i][j] and maps[i][j] == maps[i][j-1]: # 동일?
                    maps[i][j] += maps[i][j]
                    maps[i][j-1] = 0
                    
    elif d == 3: # 좌
        for j in range(n-1): # 좌부터 탐색
            for i in range(n):
                if maps[i][j] and maps[i][j] == maps[i][j+1]: # 동일?
                    maps[i][j] += maps[i][j]
                    maps[i][j+1] = 0
    return maps


def game(cnt, orign_maps):
    global maxima
    if cnt == 5: # 다섯번 이동해서 가장 큰 블록의 값
        maxima = max(maxima, max(map(max, orign_maps)))
        return
    else:
        for d in range(4): # 4방향 중 한 방향으로 이동
            n_maps = move(deepcopy(orign_maps), d) # 이동
            nn_maps = plus(deepcopy(n_maps), d) # 결합
            nnn_maps = move(deepcopy(nn_maps), d) # 이동
            game(cnt+1, deepcopy(nnn_maps))

n = int(stdin.readline())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
maxima = 0

game(0, maps)
print(maxima)