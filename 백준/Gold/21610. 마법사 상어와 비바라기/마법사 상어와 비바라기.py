# 21610 마법사 상어와 비바라기
# 칸에 있는 물의 양을 의미 
# 가장 위 = 1, 1
# 가장 오른쪽과 왼쪽 연결 + 가장 위쪽과 아랫쪽 연결 

# (N-1, 0) (N-1, 1), (N-2, 0), (N-2, 1)에 구름 생김
# 구름에 이동을 명령한다. 모든 구름이 d방향으로 s칸 이동함 
# 각 구름에서 비가 내려 구름이 있는 칸에 물의 양이 1증가함 
# 구름이 모두 사라짐 
# 2에서 증가한 칸에서 대각선 방향으로 거리가 1인 칸에 있는 
# 물이 있는  바구니의 수 만큼 maps[r][c] 증가 (경계를 넘어가는건 배제)
# 바구니에 저장된 물의 양이 2이상인 모든 칸에 구름이 생기고 물의 양이 2 줄어듬 
# 이때 구름이 생기는 칸은 구름이 사라진 칸이 아니어야 한다. 
from sys import stdin 
n, m = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
move = []
for _ in range(m):
    move.append(list(map(int, stdin.readline().split())))
    
dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
diagx, diagy = [1, 1, -1, -1], [1, -1, 1, -1]
cld = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
move = move[::-1]
while(move):
    d, s = move.pop()
    d = d-1
    cloud = [[0]*n for _ in range(n)]
    
    for i in range(len(cld)):
        cld[i][0], cld[i][1] = (cld[i][0] + s*dx[d])%n, (cld[i][1] + s*dy[d])%n #모든 구름이 d방향으로 s칸 이동한다. 
        cloud[cld[i][0]][cld[i][1]] = 1
    for i in range(len(cld)):
        maps[cld[i][0]][cld[i][1]] += 1 # 구름이 있는 칸에 물 양이 1 증가함 
    
    for i in range(len(cld)):
        cnt = 0
        for k in range(4):
            a, b = cld[i][0] + diagx[k], cld[i][1] + diagy[k]
            if 0 <= a <= n-1 and 0<= b <= n-1:
                if maps[a][b]: cnt += 1 # 대각선 방향에 물이 있다면 물 복사 버그
                    
        maps[cld[i][0]][cld[i][1]] += cnt
    
    n_cld = []
    
    for i in range(n):
        for j in range(n):
            if maps[i][j] >= 2 and not cloud[i][j]:
                n_cld.append([i, j])
                maps[i][j] -= 2

    cld = n_cld
ans = 0
for i in range(n):
    ans += sum(maps[i])
print(ans)