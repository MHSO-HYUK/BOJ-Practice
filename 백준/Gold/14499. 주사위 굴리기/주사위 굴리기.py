# 14499 주사위 굴리기
# 이동한 칸이 0인 경우 주사위 바닥면이 바닥으로 복사된다.
# 이동한 칸이 0이 아닌 경우에는 칸에 적힌 수가 바닥면으로 복사된다.


from sys import stdin

n, m, x, y, k = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split()))for _ in range(n)]
command = list(map(int, stdin.readline().split()))
command.reverse()
dice = [0] * 6 # 앞 뒤 위 아래 좌 우 순으로 !
dx, dy= [0, 0, -1, 1], [1, -1, 0, 0] # 1, 2, 3, 4 // 동 서 북 남
## 동 // 앞 뒤 위 아래 좌 우 -> 앞 뒤 우 좌 위 아래
## 서 // 앞 뒤 위 아래 좌 우 -> 앞 뒤 좌 위 아래 위
## 남 // 앞 뒤 위 아래 좌 우 -> 아래 위 앞 뒤 좌 우
## 북 // 앞 뒤 위 아래 좌 우 -> 위 아래 뒤 앞 좌 우
i, j = x, y
while(command):
    k = command.pop()
    a, b = i + dx[k-1], j+dy[k-1]
    if 0<=a<=n-1 and 0<=b<=m-1:
        if k == 1:
            dice = [dice[0], dice[1], dice[5], dice[4], dice[2], dice[3]]
        elif k == 2:
            dice = [dice[0], dice[1], dice[4], dice[5], dice[3], dice[2]]
        elif k == 3:
            dice = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]
        elif k == 4:
            dice = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]

        if not maps[a][b]:
            maps[a][b] = dice[3]

        else:
            dice[3] = maps[a][b]
            maps[a][b] = 0

        i, j = a, b
        print(dice[2])