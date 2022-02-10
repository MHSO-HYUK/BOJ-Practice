#3055 탈출
# 빈공간 . // 물 * // 돌 X // 굴 D // 고슴도치 S
# 물은 비어있는 칸으로 확장 
# 다음 시간이 물이 찰 예정인 칸으로 이동 불가! 
from sys import stdin
from collections import deque
def water():
    q = deque()
    for i in range(n):
        for j in range(m):
            if(maps[i][j] == '*'):
                q.append([i, j])
                
    while(q):
        x, y = q.popleft()
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if(0<= a <= n-1 and 0<=b<=m-1):
                if(maps[a][b] == '.'):
                    maps[a][b] = '*'
        
def move():
    global d
    queue = deque([[d[0], d[1], 0]]) # x, y, cnt
    visit = [[0 for _ in range(m)] for _ in range(n)]
    while(queue):
        water()
        for _ in range(len(queue)):
            x, y, cnt = queue.popleft()
            if(maps[x][y] == 'D'):
                return cnt
            
            for k in range(4):
                a, b = x+dx[k], y+dy[k]
                if(0<=a<=n-1 and 0<=b<=m-1):
                    if((maps[a][b] == '.' or maps[a][b] == 'D') and visit[a][b] == 0):
                        visit[a][b] = 1
                        queue.append([a, b, cnt+1])
    return 'KAKTUS'          

n, m = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(stdin.readline().rstrip()))
dx, dy = [1, -1, 0 ,0], [0, 0, 1, -1]
w = []
for i in range(n):
    for j in range(m):
        if(maps[i][j] == '.'):
            w.append([i, j])
        if(maps[i][j] == 'S'):
            d = [i, j]

print(move())