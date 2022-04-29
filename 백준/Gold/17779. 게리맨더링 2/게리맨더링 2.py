# 17779 게리맨더링 2
from sys import stdin
def check(x, y, d1, d2):
    global total
    line = [[0 for _ in range(n+1)] for _ in range(n+1)]
    # 경계선 : x-1, y-1    +1 , -1      x+d1-1, y-d1-1
    #            x-1, y-1,     +1  + 1   x+d2-1, y+d2 -1
    #            x+d1-1, y-d1-1  +1 + 1    x+d1+d2-1  y-d1+d2-1
    #            x+d2-1, y+d2-1,   +1 -1   x+d2+d1-1, y+d2-d1-1
    sx, sy = x, y
    while(1):
        line[sx][sy] = 1
        sx += 1
        sy -= 1
        if (sx == x+d1+1 and sy == y-d1-1):
            break
        
    sx, sy = x, y
    while(1):
        line[sx][sy] = 1
        sx += 1
        sy += 1
        if sx == x+d2+1 and sy == y+d2+1:
            break
        
    sx, sy = x+d1, y-d1
    while(1):
        line[sx][sy] = 1
        sx += 1
        sy += 1
        if sx == x+d1+d2+1 and sy == y-d1+d2+1:
            break
        
    sx, sy = x+d2, y+d2
    while(1):
        line[sx][sy] = 1
        sx += 1
        sy -= 1
        if sx== x+d1+d2+1 and sy == y-d1+d2-1:
            break
        
        
    people = [0 for _ in range(5)]
    # 1번 선거구 0 <= r < x+d1-1 0 <= c <= y-1
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if line[i][j]:
                break
            people[0] += maps[i][j]
            
    # 2번 선거구 0 <= r <= x+d2-1 y-1 < c <= n-1
    for i in range(1, x+d2+1):
        for j in range(n, y, -1):
            if line[i][j]:
                break
            people[1] += maps[i][j]
            
    # 3번 선거구 x+d1-1 <= r <= n-1 0 <= c < y-d1+d2-1
    for i in range(x+d1, n+1):
        for j in range(1, y-d1+d2):
            if line[i][j]:
                break
            people[2] += maps[i][j]
            
    # 4번 선거구 x+d2-1 < r <= n-1 y-d1+d2-1 <= x <= n-1
    for i in range(x+d2+1, n+1):
        for j in range(n, y-d1+d2-1, -1):
            if line[i][j]:
                break
            people[3] += maps[i][j]
    
    # 5번 선거구 = 경계선과 그 안에 들어있는 선거구
    people[4] = total - sum(people)
    return max(people)- min(people)


n = int(stdin.readline())
maps = [[0]*(n)] + list(list(map(int, stdin.readline().split())) for _ in range(n))
for i in range(n+1):
    maps[i] = [0] + maps[i]



# d1, d2 >= 1 // 1 <= x < x+d1+d2 <= n // 1 <= y-d1 < y < y+d2 <= n
total = sum(map(sum, maps))
minima = 10**10
for d1 in range(1, n+1):
    for d2 in range(1, n+1):
        for x in range(1, n+1):
            if x+d1+d2 <= n:
                for y in range(1, n+1):
                    if 1 <= y-d1 and y+d2 <= n:
                        minima = min(minima, check(x, y, d1, d2))
print(minima)