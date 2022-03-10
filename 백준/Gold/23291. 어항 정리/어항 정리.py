# 23291 어항 정리
from sys import stdin 
from collections import deque
from copy import deepcopy
import sys

n, diff = map(int, stdin.readline().split())
fish= list(map(int, stdin.readline().split()))
def rotate(temp):
    new_temp = []
    for j in range(len(temp[0])):
        cache = []
        for i in range(len(temp)):
            cache.append(temp[i][j])
        new_temp.append(cache)
    new_temp.reverse()
    return new_temp
turn = 0    
while(1):
#1. 물고기가 가장 적은 어항에 물고기를 한마리 넣는다 
# 그런 어항이 여러개라면 다 넣는다. 
    if max(fish) - min(fish) <= diff:
        print(turn)
        sys.exit()
    minima = 10**10
    for i in range(n):
        minima = min(minima, fish[i])
    for i in range(n):
        if fish[i] == minima:
            fish[i] += 1
#2. 어항을 쌓는다 
# 먼저 가장 왼쪽의 어항을 그 오른쪽에 쌀음 
# 그리고 공중부양시켜 시계 방향으로 회전 시키고 올린다. 
# 이거를 반복한다. 
    up = [[fish[1]], [fish[0]]]
    now = 2
    while(1):
        for i in range(now, now+len(up)):
            up[i-now].append(fish[i])
        now = now + len(up)
        if len(up[0]) > n- now:
            last = n-now
            break
        up = rotate(up)

    maps = [[0 for _ in range(len(up) + last)] for _ in range(len(up[0]))]
    for i in range(len(up[0])):
        for j in range(len(up)):
            maps[i][j] = up[j][i]
    
    for i in range(last):
        maps[-1][-1-i] = fish[-1-i]
# 3. 공중 부양이 끝나면 어항에 있는 물고기 수를 조절한다.
# 인접한 어항에 대하여 물고기 수의 차이 // 5 가 0 보다 크면 더 많은 곳에 있는 물고기 d마리를 보낸다. (동시)
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    change = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if 0<=x<=len(maps)-1 and 0 <= y <= len(maps[0]) -1:
                    if maps[x][y] and maps[i][j]:
                        if maps[x][y] > maps[i][j]:
                            change[i][j] += (maps[x][y] - maps[i][j]) //5
                        if maps[x][y] < maps[i][j]:
                            change[i][j] -= (maps[i][j] - maps[x][y]) // 5
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            maps[i][j] += change[i][j]
    
# 4. 다시 일렬로 놓는다. 
# 가장 왼쪽의 어항부터 그리고 가장 아래에 있는 어항부터 가장 위에 있는 어항까지 순서대로 다시 놓음
    fish = []
    for j in range(len(maps[0])):
        for i in range(len(maps)-1, -1, -1):
            if maps[i][j]:
                fish.append(maps[i][j])

# 5. 이번에는 가운데를 중심으로 N/2개를 공중부양시켜 180도 회전시켜 올림 (2회 반복)
    temp1 = fish[:len(fish)//2]
    temp1.reverse()
    temp2 = fish[len(fish)//2:]
    for i in range(len(temp1)):
        temp1[i] = [temp1[i], temp2[i]]
    
    temp3 = temp1[:len(temp1)//2]
    temp3.reverse()
    temp4 = temp1[len(temp1)//2:]
    for i in range(len(temp3)):
        temp3[i].reverse()
        temp3[i] = temp3[i]+ temp4[i]
    maps = deepcopy(temp3)
    change = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if 0<=x<=len(maps)-1 and 0 <= y <= len(maps[0]) -1:
                    if maps[x][y] and maps[i][j]:
                        if maps[x][y] > maps[i][j]:
                            change[i][j] += (maps[x][y] - maps[i][j]) //5
                        if maps[x][y] < maps[i][j]:
                            change[i][j] -= (maps[i][j] - maps[x][y]) // 5
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            maps[i][j] += change[i][j]
    fish = []
# 6. 다시 인접한 어항에 대해 분배
    for i in range(len(maps)):
        for j in range(len(maps[0])-1, -1, -1):
            fish.append(maps[i][j])
    turn += 1
