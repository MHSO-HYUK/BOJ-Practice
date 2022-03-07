# 17143 낚시왕
from sys import stdin

n, m, k = map(int, stdin.readline().split())
info = [[] for _ in range(k)]
loc = [[] for _ in range(k)]
visit = [[-1 for _ in range(m+1)] for _ in range(n+1)]
dx, dy = (0, -1, 1, 0 ,0), (0, 0, 0, 1, -1)
for i in range(k):
    x, y, s, d, z = map(int, stdin.readline().split())
    loc[i] = [x, y]
    visit[x][y] = i
    if d <= 2:
        s %= 2*(n-1)
    else:
        s %= 2*(m-1)
    info[i]= [s, d, z]
    # x, y, 속력, 방향 , 크기 // d = 1 위 2 아래 3 오른쪽 4 왼쪽

# 낚시왕이 오른쪽으로 한칸 이동
# 낚시왕이 열에 있는 상어중 가장 높은 놈을 잡는다
# 상어가 이동
p, score = 1, 0
while(1):
    if p == m+1:
        break

    temp, minima = -1, 10**10
    for i in range(1, n+1):
        if visit[i][p] != -1:
            loc[visit[i][p]] = 0
            score += info[visit[i][p]][2]
            break

    visit = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(k):
        if loc[i]:
            x, y = loc[i]
            cnt = 0
            while(cnt != info[i][0]):
                nx, ny = x + dx[info[i][1]], y + dy[info[i][1]]
                if 1 <= nx <= n and 1 <= ny <= m:
                    cnt += 1
                    x, y = nx, ny
                else:
                    if info[i][1] % 2:
                        info[i][1] += 1
                        nx, ny = x + dx[info[i][1]], y + dy[info[i][1]]
                        cnt += 1
                        x, y = nx, ny
                    else:
                        info[i][1] -= 1
                        nx, ny = x + dx[info[i][1]], y + dy[info[i][1]]
                        cnt += 1
                        x, y = nx, ny

            if visit[x][y] != -1:
                if info[visit[x][y]][2] > info[i][2]:
                    loc[i] = 0
                else:
                    loc[visit[x][y]] = 0
                    visit[x][y] = i
                    loc[i] = [x, y]
            else:
                visit[x][y] = i
                loc[i] = [x, y]
    p += 1
print(score)