# 17822 원판 돌리기
from sys import stdin
from collections import deque
def bfs(x, y, num):
    global flag
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = deque([[x, y]])
    visit[x][y] = 1
    cache = [[x, y]]
    while(queue):
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if not (0 < nx <= n and 0 <= ny <= m-1):
                if nx > n or nx < 1: # 원판이 아예 경계를 넘는 경우
                    continue
                if ny > m-1:
                    ny -= m
                elif ny < 0:
                    ny += m
                    
            if circle[nx][ny] == num and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                cache.append([nx,ny])
                queue.append([nx,ny])

    if len(cache)>= 2:
        flag = True
        for a, b in cache:
            circle[a][b] = 0

# 원판의 회전은 독립적
n, m, t =map(int, stdin.readline().split())
circle = [0] + [[] for _ in range(n)]
for i in range(n):
    circle[i+1] = list(map(int, stdin.readline().split()))
comm = deque()
for _ in range(t):
    comm.append(list(map(int, stdin.readline().split())))

while(comm):
    a,d,k = comm.popleft()
    k %= m
    for x in range(a, n+1, a):
        if d == 0: # 시계방향
            circle[x] = circle[x][-k:m] + circle[x][0:m-k] 
        else: # 반시계방향 
            circle[x] = circle[x][k:m] + circle[x][0:k]
        # 원판에 수가 남아 있으면 인접하면서 수가 같은 것을 모두 찾는다.
    # 그러한 수가 있다면 원판에서 인접하면서 같은 수를 모두 지움
    # 없다면 원판에 적힌 수의 평균을 구하고 평균보다 작으면 1을 빼고 작으면 1을 더함
    visit = [[0 for _ in range(m)] for _ in range(n+1)]
    flag = False
    cnt = 0
    for i in range(1, n+1):
        for j in range(m):
            if not visit[i][j] and circle[i][j]:
                cnt += 1
                bfs(i, j, circle[i][j])

    if not flag:
        total = 0
        for i in range(1, n+1):
            total += sum(circle[i])
        for i in range(1, n+1):
            for j in range(m):
                if circle[i][j]:
                    if circle[i][j] > total / cnt:
                        circle[i][j] -= 1
                    elif circle[i][j] < total / cnt:
                        circle[i][j] += 1
ans = 0
for i in range(1, n+1):
    ans += sum(circle[i])
print(ans)