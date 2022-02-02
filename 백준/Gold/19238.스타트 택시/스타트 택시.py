#19238 스타트 택시
#최단 거리가 가장 짧은 승객을 고른다 -> 여러명이면 위쪽 >왼쪽 작은 순으로 
#연료 칸당 -1, 
#목적지로 이동하면 태운 뒤 소모 연료의 두배 충전 
from collections import deque
from sys import stdin
import heapq
def go(drive): #승객 태우는 함수
    global m, n, fuel
    visit = [[-1 for _ in range(n)] for _ in range(n)]
    visit[drive[0]][drive[1]] = 0
    queue = deque([[drive[0], drive[1]]])
    while(queue):
        x, y = queue.popleft()
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if(0<=a<=n-1 and 0<=b<=n-1):
                if(maps[a][b] == 0 and visit[a][b] == -1):
                    visit[a][b] = visit[x][y] + 1
                    queue.append([a,b])       
    flag = False
    for i in range(m):
        if(guest[i][0] == 0):
            flag = True
            if(visit[guest[i][1][0]][guest[i][1][1]] == -1):
                print(-1)
                return 0
            guest[i][3] = visit[guest[i][1][0]][guest[i][1][1]]
    if(not flag):
        print(fuel)
    elif(flag):
        minima = 10**10
        same = []
        heapflag = False
        for i in range(m):
            if(guest[i][0] == 0):
                if(guest[i][3] < minima):
                    same = []
                    heapq.heappush(same, [guest[i][1][0], guest[i][1][1], i])
                    minima = guest[i][3]
                    temp = i
                elif(guest[i][3] == minima):
                    heapflag = True
                    heapq.heappush(same, [guest[i][1][0], guest[i][1][1], i])
                    
        if(heapflag):
            p, q, temp = heapq.heappop(same) 
        guest[temp][0] = 1
        fuel -= minima
        if(fuel < 0):
            print(-1)
        else:
            out(guest[temp])

def out(road): #승객 내리는 함수
    global m, n, fuel
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[road[1][0]][road[1][1]] = 0
    queue = deque([[road[1][0], road[1][1]]])
    while(queue):
        x, y = queue.popleft()
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if(0<=a<=n-1 and 0<=b<=n-1):
                if(maps[a][b] == 0 and visited[a][b] == -1):
                    visited[a][b] = visited[x][y] + 1
                    queue.append([a,b])
    dest = visited[road[2][0]][road[2][1]]
    if(dest == -1):
        print(-1)
        return 0
    fuel -= dest
    if(fuel < 0):
        print(-1)
    else:
        fuel += 2 * (dest)
        go(road[2])

n, m, fuel = map(int, stdin.readline().split()) #fuel : 초기 연료량
maps = []
for _ in range(n): #지도의 크기
    maps.append(list(map(int, stdin.readline().split()))) #0 빈칸 , 1 벽
a, b = list(map(int, stdin.readline().split()))
driver = [a-1, b-1]
guest = []
for _ in range(m): #승객의 수
    a,b,c,d = map(int, stdin.readline().split())
    guest.append([0,[a-1,b-1], [c-1,d-1], 10**10])
dx, dy = [1,-1,0,0],[0,0,1,-1]
go(driver)