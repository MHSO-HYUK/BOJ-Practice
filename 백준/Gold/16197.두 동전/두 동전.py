#둘중 하나만 떨어뜨리기
from sys import stdin
from collections import deque
def coin():
    mapp = ['#', '.'] 
    while(queue):
        ax, ay, bx, by, cnt = queue.popleft()
        if cnt >= 10:
            return -1
        for k in range(4):
            Ax, Ay = ax+dx[k], ay+dy[k] 
            Bx, By = bx+dx[k], by+dy[k]
            movingA = [[ax, ay], [Ax, Ay]]
            movingB = [[bx, by], [Bx, By]]
            if(not (Ax<0 or Ay < 0 or Ax>n-1 or Ay > m-1) and (Bx<0 or By < 0 or Bx>n-1 or By > m-1)):
                return cnt
            if((Ax<0 or Ay < 0 or Ax>n-1 or Ay > m-1) and not (Bx<0 or By < 0 or Bx>n-1 or By > m-1)):
                return cnt
            
            if(0 <= Ax <= n-1 and 0 <= Bx <= n-1 and 0<= Ay <= m-1 and 0 <= By <= m-1):
                for i in range(2):
                    for j in range(2):
                        if maps[Ax][Ay] == mapp[i] and maps[Bx][By] == mapp[j]:
                                temp = movingA[i] + movingB[j]
                                temp.append(cnt+1)
                                queue.append(temp)
    return -1

n, m = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(stdin.readline().rstrip()))
queue = deque()
v = []
for i in range(n):
    for j in range(m):
        if(maps[i][j] == 'o'):
            v.append(i)
            v.append(j)
            maps[i][j] = '.'
            
queue.append([v[0], v[1], v[2], v[3], 0])
dx, dy = [1,-1,0,0], [0,0,1,-1]

ans = coin()

if(ans == -1):
    print(ans)
else:
    print(ans + 1)