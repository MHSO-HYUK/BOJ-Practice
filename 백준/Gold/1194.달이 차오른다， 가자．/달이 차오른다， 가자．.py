#1194 달이 차오른다, 가자
from collections import deque
from sys import stdin
def moon(i, j):
    queue = deque([[i,j,0,0]])
    visit = [[[False] * (1<<6) for _ in range(50)] for _ in range(50)]
    visit[i][j][0] = True
    while(queue):
        x, y, key, c = queue.popleft()
        if(maps[x][y] == '1'): return c
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if(a<0 or b<0 or a>n-1 or b>m-1): #맵 범위 초과
                continue     
            if(not visit[a][b][key]):
                if(maps[a][b] == '1' or maps[a][b] == '.'): #도착
                    visit[a][b][key] = True 
                    queue.append([a, b, key, c+1])
                if 'a' <= maps[a][b] <= 'f':
                    temp = key | (1<<(ord(maps[a][b]) - ord('a')))
                    visit[a][b][temp] = True
                    queue.append([a,b,temp,c+1])
                if 'A' <= maps[a][b] <= 'Z':
                    val = key & (1<<(ord(maps[a][b]) - ord('A')))
                    if(val):
                        visit[a][b][key] = True
                        queue.append([a,b,key,c+1])
    return -1
                
n, m = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(stdin.readline().rstrip()))
dx, dy = [1,-1,0,0],[0,0,1,-1]
for i in range(n):
    for j in range(m):
        if(maps[i][j] == '0'):
            maps[i][j] = '.'
            print(moon(i,j))
            break