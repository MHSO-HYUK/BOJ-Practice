# 5213 과외맨
from sys import stdin
from collections import deque, defaultdict
import sys
# 1. 마지막 타일로 이동할 수 없을 경우 -> 가장 큰 타일로
# 2. 두 타일이 인접하고 인접한 타일의 수가 같아야 한다.  
def bfs():
    dx, dy = (0, 0, 1, -1), (0, 0, 1, -1)
    queue = deque([[0, 0, [1]]])
    queue.append([0, 1, [1]])
    visit = [[10**10 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 1
    visit[0][1] = 1
    temp, maxima = [], -1
    while(queue):
        x, y, road = queue.popleft()
        if maxima <= maps[x][y][1]:
            if maxima == maps[x][y][1]:
                if len(temp) > len(road):
                    temp = road
            else:
                temp = road
                maxima = maps[x][y][1]
                
        if not x % 2:
            if not y % 2:
                for k in [[1, 0], [-1, 0], [0, -1]]:
                    nx, ny = x+k[0], y+k[1]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1 and len(maps[nx][ny]):
                        if maps[x][y][0] == maps[nx][ny][0]:
                            if visit[nx][ny] > len(road) + 1:
                                for a, b in tile[maps[nx][ny][1]]:
                                    visit[a][b] = len(road) + 1
                                    queue.append([a, b, road+[maps[a][b][1]]])
                            
                    
            else:
                for k in [[1, 0], [-1, 0], [0, 1]]:
                    nx, ny = x+k[0], y+k[1]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1 and len(maps[nx][ny]):
                        if maps[x][y][0] == maps[nx][ny][0]:
                            if visit[nx][ny] > len(road) + 1:
                                for a, b in tile[maps[nx][ny][1]]:
                                    visit[a][b] = len(road) + 1
                                    queue.append([a, b, road+[maps[a][b][1]]])

        else:
            if not y % 2:
                for k in [[1, 0],[-1, 0], [0, 1]]:
                    nx, ny = x+k[0], y+k[1]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1 and len(maps[nx][ny]):
                        if maps[x][y][0] == maps[nx][ny][0]:
                            if visit[nx][ny] > len(road) + 1:
                                for a, b in tile[maps[nx][ny][1]]:
                                    visit[a][b] = len(road) + 1
                                    queue.append([a, b, road+[maps[a][b][1]]])
                
            else:
                for k in [[1, 0], [-1, 0], [0, -1]]:
                    nx, ny = x+k[0], y+k[1]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1 and len(maps[nx][ny]):
                        if maps[x][y][0] == maps[nx][ny][0]:
                            if visit[nx][ny] > len(road) + 1:
                                for a, b in tile[maps[nx][ny][1]]:
                                    visit[a][b] = len(road) + 1
                                    queue.append([a, b, road+[maps[a][b][1]]])
    print(len(temp))
    print(*temp)
n = int(stdin.readline())
maps = []
tile = defaultdict(int)
flag, out, cache =True, True, []
num, row = 1, 0
while(1):
    if flag:
        cache = []
        for i in range(n):
            try:
                a, b= map(int, stdin.readline().split())
                tile[num+i] = [[row, 2*i], [row, 2*i+1]]
            except:
                out = False
                break
            cache.append([a, num+i])
            cache.append([b, num+i])
        if not out:
            break
        maps.append(cache)
        flag = not flag
        num += n
        row+=1
    else:
        cache = [[]]
        for i in range(n-1):
            try:
                a, b= map(int, stdin.readline().split())
                tile[num+i] = [[row, 2*i+1], [row, 2*i+2]]
            except:
                out = False
                break
            cache.append([a, num+i])
            cache.append([b, num+i])
        if not out:
            break
        cache.append([])
        maps.append(cache)
        flag = not flag
        num += n-1
        row += 1

n, m = len(maps), len(maps[-1])
bfs()