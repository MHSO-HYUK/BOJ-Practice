import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = []
for _ in range(n):
  maps.append(list(map(int, input().split()))) # 0 빈칸, 1 벽, 2 청소기or청소한곳
possible = True
dx = [-1, 0, 1, 0] # d= 0 북쪽, 1 동쪽, 2 남쪽, 3 서쪽
dy = [0, 1, 0, -1]

maps[r][c] = 2
x, y = r, c
while True:
  cleans = False # 왼쪽 청소 했는지?
  for i in range(4): # 왼쪽 청소하기
    nx = x + dx[(d+3-i)%4]
    ny = y + dy[(d+3-i)%4]
    if maps[nx][ny] == 0: # 왼쪽에 청소가 된다면
      x, y = nx, ny
      d = (d+3-i)%4
      maps[x][y] = 2
      cleans = True
      break
  if cleans: # 왼쪽 청소했음
    continue
  nx = x + dx[(d+2)%4] # 네방향 모두 청소못한경우 뒤로 후진
  ny = y + dy[(d+2)%4]
  if maps[nx][ny] == 1: # 뒤가 벽이라면 
    possible = False
  else:
    x, y = nx, ny # 벽이 아니면
  if not possible:
      break
      
count = 0
for i in range(n):
  for j in range(m):
    if maps[i][j] == 2:
      count += 1
print(count)