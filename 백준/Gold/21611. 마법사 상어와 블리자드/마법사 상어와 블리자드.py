# 21611 마법사 상어와 블리자드
from sys import stdin

n, m = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
num = [[0 for _ in range(n)] for _ in range(n)]
com = list(list(map(int, stdin.readline().split())) for _ in range(m))
# 파괴 -> 이동 -> 폭발 -> 이동 -> 변화
# 방향 d로 s만큼의 칸에 던져 파괴한다. (벽은 파괴 X)
# 만약 A의 번호보다 번호가 하나 작은 칸이 빈칸이면 구슬은 그 빈칸으로 이동한다. 
# 4개 이상 연속하는 구슬이 있으면 폭발한다. (연속해서 가능)
# 더 이상 폭발할 구슬이 없으면 변화
# 연속하는 구슬 = 그룹 -> A, B로 변함 A = 구슬의 갯수 B = 구슬의 번호
com = com[::-1]
score = [0, 0, 0]
x, y = n // 2, n // 2
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
k, level, cnt, go, p = 3, 1, 0, 0, 1 # 방향 좌측 거리 1
bizz = [0 for _ in range(n**2)]
while(1):
    if x == 0 and y == 0:
        break
    nx, ny = x+dx[k], y+dy[k]
    num[nx][ny] = p
    bizz[p] = maps[nx][ny]
    x, y = nx, ny
    go += 1
    p += 1
    if level == go:
        if k==1: k=3
        elif k==2: k=4
        elif k==3: k=2
        elif k==4: k=1
        cnt += 1
        go = 0
    if cnt == 2:
        cnt = 0
        level += 1

x, y = n // 2, n // 2
while(com):
    d, s = com.pop()
    # 파괴
    r = 1
    while(r <= s):
        nx, ny = x + r * dx[d], y + r *dy[d]
        maps[nx][ny] = 0
        bizz[num[nx][ny]] = 0
        r += 1

    while(1):
        # 이동 
        pocket = []
        for i in range(1, len(bizz)):
            if bizz[i]:
                pocket.append(bizz[i])
        bizz = [0] + pocket + [0 for i in range(n**2-1-len(pocket))]
        for i in range(n):
            for j in range(n):
                maps[i][j] = bizz[num[i][j]]
        # 폭발
        bflag = False
        cnt = 1
        for i in range(1, len(bizz)-1):
            if bizz[i] == bizz[i+1]:
                cnt += 1
            else:
                if cnt >= 4:
                    bflag = True
                    score[bizz[i]-1] += cnt
                    for k in range(i, i-cnt, -1):
                        bizz[k] = 0
                cnt = 1
                
        if not bflag:
            break

    new_bizz, cnt = [0], 1
    for i in range(1, n**2-1):
        if bizz[i] == bizz[i+1]:
            cnt += 1
        else:
            new_bizz.append(cnt)
            new_bizz.append(bizz[i])
            cnt = 1
    if len(new_bizz) >= n**2:
        new_bizz = new_bizz[:n**2]
    else:
        new_bizz = new_bizz + [0 for i in range(n**2-len(new_bizz))]
    bizz = new_bizz
    for i in range(n):
        for j in range(n):
            maps[i][j] = bizz[num[i][j]]
    
print(score[0] + 2*score[1] + 3*score[2])