# 17406 배열 돌리기 4
# 배열의 값 = 행의 합 중 최솟값
from sys import stdin
from itertools import permutations
from copy import deepcopy
from collections import deque
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] #우 하 좌 상
def rotate(x, y, s):
    global temp
    cache = deque()
    while(s):
        for j in range(y-s, y+s):
            cache.append(temp[x-s][j])
        for j in range(x-s, x+s):
            cache.append(temp[j][y+s])
        for j in range(y+s, y-s, -1):
            cache.append(temp[x+s][j])
        for j in range(x+s, x-s, -1):
            cache.append(temp[j][y-s])

        for j in range(y-s+1, y+s):
            temp[x-s][j] = cache.popleft()
        for j in range(x-s, x+s):
            temp[j][y+s] = cache.popleft()
        for j in range(y+s, y-s, -1):
            temp[x+s][j] = cache.popleft()
        for j in range(x+s, x-s, -1):
            temp[j][y-s] = cache.popleft()

        temp[x-s][y-s] = cache.popleft()
        s -= 1

n, m, k = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
comm = []
for _ in range(k):
    r, c, s = map(int, stdin.readline().split())
    comm.append([r-1, c-1, s]) 
# [r, c]를 중심으로 s칸이 시계 방향으로 돌아감 
minima = 10**10
for seq in permutations(range(len(comm)), len(comm)):
    temp = deepcopy(maps)
    for i in seq:
        rotate(comm[i][0], comm[i][1], comm[i][2])

    ans = 10**10
    for i in range(len(temp)):
        ans = min(ans, sum(temp[i]))

    minima = min(minima, ans)

print(minima)