# 3190 뱀 
# 사과를 먹으면 길이가 늘어남
# 벽이나 자기랑 부딫히면 게임 끝남
# 0, 0 시작 -> 길이 1 // 처음 오른쪽 향함
# 몸을 늘려 머리를 다음 칸으로 // 사과가 있다면 사과 없어짐
# 사과 없다면 꼬리를 비움
from sys import stdin
n, k = int(stdin.readline()), int(stdin.readline())
maps = [[0]*(n+1) for _ in range(n+1)]
maps[0] = [3] * (n+1)
for i in range(n+1):
    maps[i][0] = 3
for _ in range(k):
    a, b = map(int, stdin.readline().split())
    maps[a][b] = 2
l = int(stdin.readline())
time, dic = [], []
for _ in range(l):
    x, c = map(str, stdin.readline().split()) # x초 뒤에 L 혹은 D로 회전 
    time.append(x)
    dic.append(c)

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1] # 아래 위 좌 우
i, j = 1, 1
p = 0
k = 3
cnt = -1
maps[i][j] = 1
tail = [[1, 1]]
while(1):
    cnt += 1
    if p < len(time) and cnt == int(time[p]):
        if dic[p] == 'D': # 우회전 // 우 -> 아래 / 아래 -> 좌 / 좌 -> 위 / 위 -> 우
            if k == 0:  k=2
            elif k == 1: k=3
            elif k == 2: k=1
            elif k == 3: k=0
        else: #좌회전 // 위->좌 / 아래->우 / 좌->아래/우->위
            if k == 0:  k=3
            elif k == 1: k=2
            elif k == 2: k=0
            elif k == 3: k=1
        p += 1
        
    a, b = i + dx[k], j + dy[k]
    if 0 <= a <= n and 0<=b <= n:
        if maps[a][b] == 2: # 사과(꼬리 그대로)
            maps[a][b] = 1
            tail.insert(0, [a, b])
            i, j = a, b
            continue
        else:
            if maps[a][b] == 3 or maps[a][b] == 1: #벽 혹은 몸
                print(cnt+1)
                break
            
            elif maps[a][b] == 0: #그냥 칸 (꼬리변화)
                maps[a][b] = 1
                maps[tail[-1][0]][tail[-1][1]] = 0
                tail.pop()
                tail.insert(0, [a, b])
                i, j = a, b
                continue
    else:
        print(cnt+1)
        break