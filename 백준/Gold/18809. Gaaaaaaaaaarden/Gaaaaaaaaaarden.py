# 18890 Gaaaaaaaaaarden
from sys import stdin
from itertools import combinations
from collections import deque
from copy import deepcopy
def bfs(tg, tr):
    global cnt, maxima
# 배양액은 매 초마다 뿌린적 없던 인접 땅으로 퍼짐
# 초록과 빨강이 동일한 시간에 도달한 땅에서는 꽃이 피어남 -> 배양액이 사라짐
# 0 호수 // 1 배양액을 뿌릴 수 없는 땅 // 2 배양액을 뿌릴 수 있는 땅
# 모든 배양액을 남김없이 사용해야 하고 모든 배양액은 서로 다른 곳에 뿌려야
    flower = [[0] * m for _ in range(n)]
    used = [[0] * m for _ in range(n)]

    temp = 0
    for a, b in tg:
        used[a][b] = 1
        temp += 1
    for a, b in tr:
        used[a][b] = 1
        temp += 1

    queue = deque()
    queue.append([tg, tr])
    while(queue):
        tg, tr = queue.popleft()
        tempg, tempr = [], []
        check = [[0] * m for _ in range(n)] # 이번 턴에 영향을 받는 땅 체크
        # 1. 초록색 배양
        for a, b in tg:
            for k in range(4):
                ga, gb = a + dx[k], b + dy[k]
                if 0 <= ga <= n-1 and 0 <= gb <= m-1:
                    if maps[ga][gb] != 0 and check[ga][gb] == 0 and not used[ga][gb]:
                        temp += 1
                        check[ga][gb] = 1
                        used[ga][gb] = 1
                        tempg.append([ga, gb])

        # 2. 빨간색 배양
        for a, b in tr:
            for k in range(4):
                ra, rb = a + dx[k], b + dy[k]
                if 0 <= ra <= n-1 and 0 <= rb <= m-1:
                    if maps[ra][rb] != 0 and check[ra][rb] == 0 and not used[ra][rb]:
                        temp += 1
                        check[ra][rb] = 2
                        used[ra][rb] = 1
                        tempr.append([ra, rb])

                    if not flower[ra][rb] and check[ra][rb] == 1: # 이미 초록색 배양이 끝난 경우
                        flower[ra][rb] = 1
                        cnt += 1
                        tempg.remove([ra, rb]) # 꽃이 핀 곳에서는 더 이상의 배양액 안 퍼짐

        if not tempg or not tempr: # 더 이상 퍼져나갈 땅이 없는 경우
            maxima = max(maxima, cnt)
            return
        elif sq - temp < maxima - cnt:
            return
        else:
            queue.append([tempg, tempr])

n, m, g, r = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))

can = []
sq = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            can.append([i, j]) # 뿌릴 수 있는 땅 리스트
        if maps[i][j]:
            sq += 1
maxima = 0
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
for green in combinations(can, g):
    for red in combinations(can, r):
        flag = True
        for da in green: # 빨강 초록에 겹치는 땅이 있다면 패스
            if flag:
                for db in red:
                    if da == db:
                        flag = False
                        break
        if not flag:
            continue
        cnt = 0
        tg, tr = deepcopy(green), deepcopy(red)
        bfs(tg, tr)


print(maxima)