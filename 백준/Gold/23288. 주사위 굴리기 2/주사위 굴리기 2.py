# 23288 주사위 굴리기
from sys import stdin 
from collections import deque
def rotate(d):
    #0위 1아래 2우 3좌 4앞 5뒤
    global dice
    if d == 0: # 좌
        dice = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]
    elif d == 1: # 위
        dice = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
    elif d == 2: # 우
        dice = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]
    else: # 아래 
        dice = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]
        
n, m, t =map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
dice = [1, 6, 3, 4, 5, 2] #위 아래 우 좌 앞 뒤
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0] # 좌 위 우 아래
d = 2
x, y = 0, 0
score = 0
for _ in range(t):
# 이동 방향으로 한 칸 구름 // 없다면 반대로 한칸 구름
# 주사위가 도착 칸에 대한 점수를 획득
# 주사위 아랫면의 점수 A와 칸 B를 비교하여 이동방향을 결정
# A > B -> 90도 시계 // B > A 90도 반시계 // A = B 변화 X
    if 0 <=x+dx[d] <=n-1 and 0<=y+dy[d]<=m-1:
        x, y = x+dx[d], y+dy[d]
    else:
        d = d-2 # 반대로 한칸 구름
        if d < 0:
            while(d<0):
                d = d + 4
        x, y = x+dx[d], y+dy[d] 
    
    rotate(d) # 주사위에 회전 적용 

    visit = [[0]*m for _ in range(n)]
    visit[x][y] = 1
    s = 0
    queue = deque([[x, y]])
    while(queue):
        i, j = queue.popleft()
        s += 1
        for k in range(4):
            a, b = i+dx[k], j+dy[k]
            if 0 <= a<= n-1 and 0<= b <=m-1:
                if not visit[a][b] and maps[a][b] ==maps[x][y]:
                    visit[a][b] = 1
                    queue.append([a, b])
                    
    score += s * maps[x][y]

    if dice[1] > maps[x][y]: # 90도 시계
        d =(d+1)%4
        
    elif dice[1] < maps[x][y]:
        d = (d-1)%4
        if d < 0:
            d = d+4
    
    
print(score)