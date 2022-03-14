# 1981 배열에서 이동
from sys import stdin
from collections import deque
def find():
    visit = [[0] * n for _ in range(n)]
    visit[0][0] = 1
    queue = deque([[0, 0]])
    while (queue):
        x, y = queue.popleft()
        if x == n - 1 and y == n - 1:
            return 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
                if l <= maps[nx][ny] <= r and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
    return 0

n = int(stdin.readline())
maps = list( list(map(int, stdin.readline().split())) for _ in range(n))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
r_max, l_min = 0, 10**10

r_max = max(r_max, max(map(max, maps)))
r_min = max(maps[0][0], maps[-1][-1])
l_max = min(maps[0][0], maps[-1][-1])
l_min = min(l_min, min(map(min, maps)))

l, r = l_min, r_min
ans = 10**10
while l_min <= l <= l_max and r_min <= r <= r_max:
    lf, rf = False, False
    if find():
        ans = min(ans, r - l)
        l += 1
        lf = True
    else:
        if lf and rf:
            l += 1
            r += 1
        else:
            r += 1
            rf = True
print(ans)
