# 21608 상어 초등학교
# 1. 비어있는 칸 중 좋아하는 학생이 인접한 칸이 가장 많은 칸
# 2. 1이 여러개이면 인접 칸중 빈 칸이 가장 많은 칸으로 자리를 정함
# 3. 2도 여러개이면 행 / 열 오름차순으로 정함 
from sys import stdin 
import heapq

n = int(stdin.readline())
seat = [0 for _ in range(n**2+1)]
seq = [0 for _ in range(n**2)]
maps = [[0]*n for _ in range(n)]
info = [[0]*n for _ in range(n)]
for i in range(n**2):
    x, *like = map(int, stdin.readline().split())
    seq[i] = x
    seat[x] = like
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
seq.reverse()
while(seq):
    now = seq.pop()
    can = []
    can_info = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0:
                can.append([i, j])
    if len(can) == 1:
        maps[can[0][0]][can[0][1]] = now
        break
    else:
        for i in range(len(can)):
            temp, temp2 = 0, 0
            for k in range(4):
                a, b = can[i][0] + dx[k], can[i][1] + dy[k]
                if 0 <= a <= n-1 and 0<= b <= n-1:
                    if maps[a][b] in seat[now]:
                        temp += 1
                    if maps[a][b] == 0:
                        temp2 += 1
            heapq.heappush(can_info, [-temp, -temp2, can[i][0], can[i][1]])    
        
        
        a, b, c, d = heapq.heappop(can_info)
        maps[c][d] = now
        continue
score = 0
for i in range(n):
    for j in range(n):
        temp = 0
        for k in range(4):
            a, b = i + dx[k], j+dy[k]
            if 0<=a<=n-1 and 0<=b<=n-1:
                if maps[a][b] in seat[maps[i][j]]:
                    temp += 1
        if temp != 0:
            score += 10**(temp-1)
            
print(score)