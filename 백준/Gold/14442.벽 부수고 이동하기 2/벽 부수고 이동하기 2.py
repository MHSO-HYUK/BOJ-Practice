#14442 벽부수고 이동하기2
from sys import stdin
from collections import deque
def breaker():
    global n, m, limit
    dx, dy = [1, -1, 0 ,0], [0, 0, 1, -1]
    queue = deque([[0,0,0,1]]) #x, y, 부신 개수, 카운트
    visit[0][0][0] = 1
    while(queue):
        x, y, num, cnt = queue.popleft()
        if(x == n-1 and y == m-1):
            return cnt
        for k in range(4):
            a, b= x + dx[k], y + dy[k]
            if(a<0 or b<0 or a>n-1 or b>m-1):
                continue
            if(num < limit):
                if(maps[a][b] == 0 and visit[a][b][num] == 0): #그냥 길을 만났음
                    visit[a][b][num] = 1
                    queue.append([a, b, num, cnt + 1])
                if(maps[a][b] == 1 and visit[a][b][num+1] == 0): # 벽을 만남(부시는 횟수 남음)
                    visit[a][b][num+1] = 1
                    queue.append([a,b,num+1, cnt+1])
            else:
                if(maps[a][b] == 0 and visit[a][b][num] == 0): #그냥 길을 만났음
                    visit[a][b][num] = 1
                    queue.append([a, b, num, cnt + 1])
    return -1
n, m, limit = map(int, stdin.readline().split()) #벽은 k개 까지 부시고 이동할 수 있다.
maps = [0 for _ in range(n)]
for i in range(n):
    maps[i] = list(map(int,stdin.readline().rstrip()))
visit = [[[0]*(limit+1) for _ in range(m)] for _ in range(n)] 
print(breaker())