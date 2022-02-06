#17836 공주님을 구해라
# 0,0 출발 -> n-1, m-1 가기
import sys
from sys import stdin
from collections import deque
def rescue():
    queue = deque([[0,0,0,0]]) #x, y, 시간, 검
    visit[0][0][0] = 1
    while(queue):
        x, y, cnt, sword = queue.popleft()
        if(x == n-1 and y== m-1):
            print(cnt)
            sys.exit()
        if(cnt > t):
            print('Fail')
            sys.exit()
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if(0<=a<=n-1 and 0<=b<=m-1):
                if(sword == 0):
                    if(maps[a][b] == 0 and visit[a][b][0] == 0):
                        visit[a][b][0] = 1
                        queue.append([a,b,cnt+1, 0])
                    if(maps[a][b] == 2 and visit[a][b][1] == 0):
                        visit[a][b][1] = 1
                        queue.append([a, b, cnt+1, 1])
                        
                if(sword == 1):
                    if(visit[a][b][1] == 0):
                        visit[a][b][1] = 1
                        queue.append([a,b,cnt+1, 1])
    print('Fail') 

n,m,t = map(int, stdin.readline().split())
maps = []
visit = [[[0,0] for _ in range(m)] for _ in range(n)]
for _ in range(n):
    maps.append(list(map(int, stdin.readline().split())))
dx, dy = [1,-1,0,0],[0,0,1,-1]
rescue()
