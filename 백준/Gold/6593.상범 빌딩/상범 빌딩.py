#6593 상범 빌딩
from sys import stdin 
from collections import deque

def sangbum(s, e):
    global l, r, c
    queue = deque()
    queue.append([s[0], s[1], s[2], 1])
    visit = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    while(queue):
        x, y, z, cnt = queue.popleft()
        for k in range(6):
            a, b, d = x+dx[k], y+dy[k], z+dz[k]
            if([a, b, d] == e):
                return f'Escaped in {cnt} minute(s).'
            
            if(0<=a<=l-1 and 0<=b<=r-1 and 0<=d<=c-1):
                if(visit[a][b][d] == 0 and (maps[a][b][d] == '.' or maps[a][b][d] == 'E')):
                    visit[a][b][d] = 1
                    queue.append([a, b, d, cnt + 1])

    return 'Trapped!'

while(1): 
    l, r, c = map(int, stdin.readline().split()) #층수 // 행 // 열 
    if([l,r,c] == [0,0,0]):
        break
        
    maps = [[] for _ in range(l)]
    for i in range(l):
        for _ in range(r):
            maps[i].append(list(stdin.readline().rstrip()))
        stdin.readline()
    dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
    for i in range(l):
        for j in range(r):
            for z in range(c):
                if(maps[i][j][z] == 'S'):
                    start = [i, j, z]
                if(maps[i][j][z] == 'E'):
                    end = [i, j, z]
    print(sangbum(start, end))