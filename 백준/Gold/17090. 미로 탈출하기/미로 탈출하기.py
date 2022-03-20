# 17090 미로 탈출하기
from sys import stdin
from collections import deque
def bfs():
    global ans
    while (queue):
        i, j = queue.popleft()
        visit[i][j] = 1
        ans += 1
        for k in range(4):
            a, b = i + dx[k], j + dy[k]
            if 0 <= a <= n-1 and 0 <= b <= m-1:
                if i == a + move[maps[a][b]][0] and j == b + move[maps[a][b]][1]:
                    if not visit[a][b]:
                        visit[a][b] = 1
                        queue.append([a, b])

n, m = map(int, stdin.readline().split())
maps = list(list(stdin.readline().rstrip()) for _ in range(n))
check = [[0 for _ in range(m)] for _ in range(n)]
ans = 0
move = {'U': [-1, 0], 'R' : [0, 1], 'D': [1, 0], 'L' : [0, -1]}
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
visit = [[0 for _ in range(m)] for _ in range(n)]
queue = deque()
for i in range(n):
    if maps[i][0] == 'L':
        queue.append([i, 0])
    if maps[i][m-1] == 'R':
        queue.append([i, m-1])
for j in range(m):
    if maps[0][j] == 'U':
        queue.append([0, j])
    if maps[n-1][j] == 'D':
        queue.append([n-1, j])

bfs()
print(ans)