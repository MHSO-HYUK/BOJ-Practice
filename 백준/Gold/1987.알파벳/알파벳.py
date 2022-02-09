#1987 알파벳
from sys import stdin 
def alpha(i, j):
    global cnt, maxima
    maxima = max(maxima , cnt)
    for k in range(4):
        a, b = i+dx[k], j+dy[k]
        if(0<=a<=n-1 and 0<=b<=m-1):
            if(not dic[ord(maps[a][b])]):
                dic[ord(maps[a][b])] = True
                cnt += 1                
                alpha(a, b)
                dic[ord(maps[a][b])] = False
                cnt -= 1
    return maxima

n, m = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(stdin.readline().rstrip()))
    
dx, dy = [1,-1, 0, 0], [0, 0, 1, -1]
dic = {i: False for i in range(ord('A'), ord('Z') + 1)}
dic[ord(maps[0][0])] = True
cnt, maxima = 1, 1
print(alpha(0, 0))