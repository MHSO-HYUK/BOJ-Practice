# 17267 상남자
# 위아래로만 간다. 
# 친구가 왼쪽으로 l번 오른쪽으로 r번 이동하도록 도와준다. 
from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
l, r = map(int, stdin.readline().split())

maps = []
for i in range(n):
    temp = list(map(int, stdin.readline().rstrip()))
    for j in range(m):
        if temp[j] == 2:
            start = [i, j]
    maps.append(temp)
queue = deque()
visit = [[[] for _ in range(m)] for _ in range(n)]
check = [[0]*m for _ in range(n)]
queue.append([start[0], start[1], l, r])
visit[start[0]][start[1]].append([l, r])
dx, dy = (1, -1), (0, 0)
while(queue):
    x, y, nl, nr = queue.popleft()
    check[x][y] = 1
    for k in range(2):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            if not maps[nx][ny] and not [nl, nr] in visit[nx][ny]:
                if not visit[nx][ny]:
                    visit[nx][ny].append([nl, nr])
                    queue.append([nx, ny, nl, nr])
                else:
                    vl, vr = visit[nx][ny][0]
                    if nl > vl or nr > vr:
                        visit[nx][ny].append([nl, nr])
                        queue.append([nx, ny, nl, nr])
                
    lx, ly = x, y-1
    rx, ry = x, y+1
    
    if nl > 0 and 0 <= lx <= n-1 and 0 <= ly <= m-1:
        if not maps[lx][ly] and not [nl-1, nr] in visit[lx][ly]:
            if not visit[lx][ly]: 
                visit[lx][ly].append([nl-1, nr])
                queue.append([lx, ly, nl-1, nr])
            else:
                vl, vr = visit[lx][ly][0]
                if nl-1 > vl or nr > vr:
                    visit[lx][ly].append([nl-1, nr])
                    queue.append([lx, ly, nl-1, nr])
            
    if nr > 0 and 0 <= rx <= n-1 and 0 <= ry <= m-1:
        if not maps[rx][ry] and not [nl, nr-1] in visit[rx][ry]:
            if not visit[rx][ry]: 
                visit[rx][ry].append([nl, nr-1])
                queue.append([rx, ry, nl, nr-1])
            else:
                vl, vr = visit[rx][ry][0]
                if nl > vl or nr -1 > vr:
                    visit[rx][ry].append([nl, nr-1])
                    queue.append([rx, ry, nl, nr-1])
print(sum(map(sum, check)))    