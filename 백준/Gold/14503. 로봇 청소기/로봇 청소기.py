# 14503 로봇 청소기
# 1 현 위치 청소
# 2 - a 현 위치 바로 왼쪽에 청소 안한 빈 곳이 존재시 왼쪽으로 회전 후 한칸 이동 후 정지 (1로 돌아감)
# 그렇지 않을 경우 왼쪽으로 회전 
# 2 - b // 2-a가 연속 네번 실행되었을 경우, 바로 뒤가 벽이라면 작동을 멈춤 + 그렇지 않다면 한 칸 후진  
from sys import stdin
import sys
n, m = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 상 우 하 좌
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
ans = 0
while(1):
    # 현위치 청소
    if not visit[r][c]:
        ans += 1
    visit[r][c] = ans
    flag4 = 0
    while(1):
        flag4 += 1
        if flag4 > 4:
            nr, nc = r - dx[d], c-dy[d]
            if maps[nr][nc] == 1:
                print(ans)
                sys.exit()
            else:
                r, c = nr, nc
                break
        new_d = d-1
        if new_d < 0:
            new_d = 3
        nr, nc = r+dx[new_d], c+dy[new_d]
        if maps[nr][nc] == 0 and not visit[nr][nc]:
            d = new_d # 왼쪽으로 회전
            r, c = nr, nc
            break
        else:
            d = new_d # 왼쪽으로 회전