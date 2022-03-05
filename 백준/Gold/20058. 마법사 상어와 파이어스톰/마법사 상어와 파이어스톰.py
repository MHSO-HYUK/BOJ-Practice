# 20058 마법사 상어와 파이어스톰
from sys import stdin 
from collections import deque
def rotate(part):
    npart = []
    for i in range(len(part)):
        temp = []
        for j in range(len(part)-1, -1, -1):
            temp.append(part[j][i])
        npart.append(temp)
    return npart

n, q = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(2**n)]
magic = list(map(int, stdin.readline().split()))
# maps // 얼음의 양을 의미
# 격자를 2**l 크기로 구분하고 90도 회전 시킴
# 얼음이 있는 칸 3개 이상과 인접하지 않은 칸은 얼음이 하나 줄음 
magic = magic[::-1]
dx, dy = [1, -1, 0 ,0], [0, 0, 1, -1]
while(magic):
    l = magic.pop()
    nmaps = [[[] for _ in range(len(maps) // 2**l)] for _ in range(len(maps) // 2**l)]
    
    
    for i in range(0, len(maps)-2**l+1, 2**l):
        for j in range(0, len(maps)-2**l+1, 2**l):
            for p in range(i, i+2**l):
                temp = []
                for q in range(j, j+2**l):
                    temp.append(maps[p][q])
                nmaps[i//2**l][j//2**l].append(temp)
            nmaps[i//2**l][j//2**l] = rotate(nmaps[i//2**l][j//2**l])
    
    
    maps = [[] for _ in range(2**n)]
    for i in range(len(nmaps)):
        for j in range(len(nmaps[i])):
            for p in range(len(nmaps[i][j])):
                    maps[len(nmaps[i][j])*i+p] += nmaps[i][j][p]
                    
                    
    
    ctemp = [[0 for _ in range(2**n)] for _ in range(2**n)]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            cnt = 0
            if maps[i][j]:
                for k in range(4):
                    x, y = i+dx[k], j+dy[k]
                    if 0<=x<=2**n-1 and 0<=y<=2**n-1:
                        if maps[x][y]:
                            cnt += 1
                ctemp[i][j] = cnt
                
    for i in range(2**n):
        for j in range(2**n):
            if ctemp[i][j] < 3 and maps[i][j]:
                maps[i][j] -= 1
                
                
ans, maxima = 0, 0
for i in range(len(maps)):
    ans += sum(maps[i])
print(ans)

visit = [[0 for _ in range(2**n)] for _ in range(2**n)]
for i in range(len(maps)):
    for j in range(len(maps[i])):
        if not visit[i][j] and maps[i][j] > 0:
            cnt = 0
            queue = deque([[i, j]])
            visit[i][j] = 1
            while(queue):
                x, y = queue.popleft()
                cnt += 1
                for k in range(4):
                    a, b= x+dx[k], y+dy[k]
                    if 0<=a<=2**n-1 and 0<=b <= 2**n-1:
                        if not visit[a][b] and maps[a][b] > 0:
                            visit[a][b] = 1
                            queue.append([a, b])
                            
        maxima = max(maxima, cnt)
print(maxima)