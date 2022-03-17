# 2933 미네랄
from sys import stdin
from collections import deque
def collapse(h, left):
    if left: # 왼쪽에서 던진 경우
        for j in range(m):
            if maps[n-h][j] == 'x':
                maps[n-h][j] = '.'
                break        
    else: # 오른쪽에서 던진 경우
         for j in range(m-1, -1, -1):
            if maps[n-h][j] == 'x':
                maps[n-h][j] = '.'
                break

def cluster(i, j):
    queue = deque([[i, j]])
    visit[i][j] = 1
    check = [[0]*m for _ in range(n)]
    check[i][j] = 1
    while(queue): # 1. 클러스터를 확인한다. 
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<= nx <= n-1 and 0<= ny <= m-1:
                if maps[nx][ny] == 'x' and not visit[nx][ny]:
                    visit[nx][ny], check[nx][ny] = 1, 1
                    queue.append([nx, ny]) 
    
    
    final, flag =10**10, False  # 2. 클러스터가 공중에 떠 있는지 확인 
    for i in range(n-1, -1, -1): # 가장 바닥부터 탐색
        for j in range(m):
            cnt = 1
            if check[i][j]: # 클러스터에 포함된 미네랄이 존재할 때,
                x, y = i+1, j
                while(1):
                    if x == n: # 한칸 더 내려가면 미네랄, 바닥과 닿는 경우
                        cnt -= 1
                        break
                    elif maps[x][y] == 'x' and not check[x][y]:
                        cnt -= 1
                        break
                    elif maps[x][y] == 'x' and check[x][y]:
                        cnt = 10**10
                        break
                    else:
                        cnt += 1 
                        x += 1
                     
                final = min(final, cnt)

    for i in range(n-1, -1, -1):
        for j in range(m):
            if check[i][j]:
                maps[i+final][j], maps[i][j] = maps[i][j], maps[i+final][j]
    

n, m = map(int, stdin.readline().split())
maps = list(list(stdin.readline().rstrip()) for _ in range(n))
s = int(stdin.readline()) # 막대를 던진 횟수
dx, dy = (1, -1, 0 ,0), (0, 0, 1, -1)
comm = deque(map(int, stdin.readline().split()))
left = True
while(comm):
    h = comm.popleft()
    
    collapse(h, left) # 미네랄을 파괴하는 함수 

    visit = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == '.':
                visit[i][j] = 1
                
    for i in range(n-1, -1, -1):
        for j in range(m):
            if not visit[i][j] and maps[i][j] == 'x':
                cluster(i, j)
     

    left = not left
    
for i in range(n):
    for j in range(m):
        print(maps[i][j], end = '')
    if i != n-1:
        print()