#16985 Maaaaaaaaaze
# 1 : 빈칸 0 : 벽 
# 판의 순서 + 회전 상태는 자유로이 정할 수 있다. 
from sys import stdin
from itertools import permutations, product
from collections import deque
def rotate(array): # 회전 알고리즘
    tuples = zip(*array[::-1])
    return [list(elem) for elem in tuples]

def miro(seq, a, b, c, d, e):
    road, queue, INF = [], deque(), 10**10 # road : 맵 상태 
    for v in seq:
        road.append(maps[v])
    move = [a, b, c, d, e]
    for i in range(5):
        while(move[i] != 0):
            road[i] = rotate(road[i])
            move[i] -= 1  
    if(road[0][0][0] == 0 or road[4][4][4] == 0): #입/출 중 벽이 존재한다면?
        return INF
    
    queue.append([0,0,0,0]) # x, y, z, cnt
    visit[0][0][0] = 1
    while(queue):
        x, y, z, cnt = queue.popleft()
        if(x == 4 and y == 4 and z == 4):
            return cnt
        for k in range(6):
            a, b, c = x+dx[k], y+dy[k], z+dz[k]
            if(0<=a<=4 and 0<=b<=4 and 0<=c<=4):
                if(road[a][b][c] == 1 and visit[a][b][c] == 0):
                    visit[a][b][c] = 1
                    queue.append([a,b,c,cnt+1])
    return INF

dx, dy, dz = [1,-1,0,0,0,0], [0,0,1,-1,0,0], [0,0,0,0,1,-1]
maps = [[],[],[],[],[]]
for i in range(5):
    for j in range(5):
        maps[i].append(list(map(int, stdin.readline().split())))
        
minima = 10**10
for k in permutations([0,1,2,3,4], 5): #판의 순서를 순열로써 모두 반영
    for a,b,c,d,e in product([0,1,2,3], repeat = 5):
        visit = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
        temp = miro(k, a, b, c, d, e)
        if(temp == 10**10):
            continue
        if(temp == 12):
            print(12)
            exit()
        else:
            minima = min(minima, temp)
            
if(minima == 10**10):
    print(-1)
else:
    print(minima)