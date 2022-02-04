# 1938 통나무 옮기기
# 회전은 3*3 구역에 나무가 하나도 없어야댐 
# 상 하 좌 우 회전, 다섯가지 이동 옵션 존재 
from collections import deque
from sys import stdin
def wood():
    while(queue):
        q,w,r,t,y,u,cnt,dirt = queue.popleft()
        if(maps[q][w] == 'E' and maps[r][t] == 'E' and maps[y][u] == 'E'):
            return cnt
        for k in range(5):
            a,b = q+dx[k],w+dy[k]
            c,d = r+dx[k],t+dy[k]
            e,f = y+dx[k],u+dy[k]
            if(k == 0 and 1<=c<=n-2 and 1<=d<=n-2 and possible[c][d] == 0):
                possible[c][d] = 1
                if(a != c): #현재 세로모양
                    queue.append([c,d-1,c,d,c,d+1,cnt+1, not dirt])
                if(a == c): #현재 가로모양
                    queue.append([c-1,d,c,d,c+1,d,cnt+1, not dirt])

            if(k != 0 and 0<=a<=n-1 and 0<=b<=n-1 and 0<=c<=n-1 and 0<=d<=n-1 and 0<=e<=n-1 and 0<=f<=n-1):
                if(not visit[c][d][dirt]):
                    if(not (maps[a][b] == '1' or maps[c][d] == '1' or maps[e][f] == '1')): #나무가 없다면
                        visit[c][d][dirt] = 1
                        queue.append([a,b,c,d,e,f,cnt+1, dirt])
                
    return 0
                    
n = int(stdin.readline())
maps = [list(stdin.readline().rstrip()) for _ in range(n)]
visit = [[[0, 0] for _ in range(n)] for _ in range(n)]
possible = [[0 for _ in range(n)] for _ in range(n)]
temp = []
checkx, checky = [1, 1, 1, 0, 0, 0, -1, -1, -1], [1, 0 ,-1, 1, 0, -1, 1, 0 ,-1]
dx, dy = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        if(maps[i][j] == 'B'):
            temp.append(i)
            temp.append(j)

temp.append(0)
if(temp[0] == temp[2]):
    visit[temp[2]][temp[3]][0] = 1
    temp.append(False)
else:
    visit[temp[2]][temp[3]][1] = 1
    temp.append(True)

for i in range(n):
    for j in range(n):
        if(not (1<=i<=n-2 and 1<=j<=n-2) or maps[i][j] == '1'):
            possible[i][j] = 1
        else:
            for k in range(9):
                a, b = i + checkx[k], j+checky[k]
                if(maps[a][b] == '1'):
                    possible[i][j] = 1      
queue = deque([temp])
print(wood())