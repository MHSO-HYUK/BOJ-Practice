# 20057 마법사 상어와 토네이도
from sys import stdin
n = int(stdin.readline())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
# 시전하면 격자의 가운데 칸 부터 토네이도의 이동이 시작된다.
dx, dy =[0, 1, 0, -1], [-1, 0, 1, 0]
# 좌 하 우 상
m = n // 2
i, j, d, level, go, twist = m, m, 0, 1, 0, 0
cnt = 0
before = sum(map(sum, maps))
while(1):
    if i == 0 and j == 0:
        break

    x, y = i + dx[d], j + dy[d]
    ax, ay = x + dx[d], y + dy[d]
    temp = 0
    total = maps[x][y]
    for k in [1, 3]:
        if 0 <= i+dx[d-k] <= n-1 and 0 <= j+dy[d-k] <= n-1:
            maps[i+dx[d-k]][j+dy[d-k]] += int(total * 0.01)
            temp += int(total * 0.01)
        else:
            cnt += int(total * 0.01)
            temp += int(total * 0.01)
        if 0 <= x + dx[d - k] <= n - 1 and 0 <= y + dy[d - k] <= n - 1:
            maps[x+dx[d-k]][y+dy[d-k]] += int(total * 0.07)
            temp += int(total * 0.07)
        else:
            cnt += int(total * 0.07)
            temp += int(total * 0.07)

        if 0 <= x + 2*dx[d - k] <= n - 1 and 0 <= y + 2*dy[d - k] <= n - 1:
            maps[x+2*dx[d-k]][y+2*dy[d-k]] += int(total * 0.02)
            temp += int(total * 0.02)
        else:
            cnt += int(total * 0.02)
            temp += int(total * 0.02)
        if 0 <= ax + dx[d - k] <= n - 1 and 0 <= ay + dy[d - k] <= n - 1:
            maps[ax+dx[d-k]][ay+dy[d-k]] += int(total * 0.1)
            temp += int(total * 0.1)
        else:
            cnt += int(total * 0.1)
            temp += int(total * 0.1)
    if 0 <= ax + dx[d] <= n - 1 and 0 <= ay + dy[d] <= n - 1:
        maps[ax+dx[d]][ay+dy[d]] += int(total * 0.05)
        temp += int(total * 0.05)
    else:
        cnt += int(total * 0.05)
        temp += int(total * 0.05)

    if 0 <= ax <= n-1 and 0 <= ay <= n-1:
        maps[ax][ay] += (total - temp)
    else:
        cnt += temp

    maps[x][y] = 0

    go += 1
    if go == level:
        d = (d + 1) % 4
        twist += 1
        go = 0
        if twist == 2:
            twist = 0
            level += 1

    i, j = x, y

after = sum(map(sum, maps))
print(before - after)

