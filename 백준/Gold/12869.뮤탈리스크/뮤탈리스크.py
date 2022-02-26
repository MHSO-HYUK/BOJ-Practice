# 12869 뮤탈리스크
from sys import stdin
def mutal(a, b, c, cnt):
    global ans   
    if a<=0 and b<=0 and c<= 0:
        ans = min(ans, cnt)
        return
    temp = [a, b, c]
    for i in range(3):
        x, y, z = temp[i]-9 if temp[i] - 9 >= 0 else 0 , temp[i-1]-3 if temp[i-1]-3 >= 0 else 0, temp[i-2]-1 if temp[i-2]-1 >=0 else 0
        if visit[x][y][z] > cnt+1:
            visit[x][y][z] = cnt+1
            mutal(temp[i]-9, temp[i-1]-3, temp[i-2]-1, cnt+1)
        x, y, z = temp[i]-9 if temp[i] - 9 >= 0 else 0 , temp[i-2]-3 if temp[i-2]-3 >= 0 else 0, temp[i-1]-1 if temp[i-1]-1 >=0 else 0
        if visit[x][y][z] > cnt+1:
            visit[x][y][z] = cnt+1
            mutal(temp[i]-9, temp[i-2]-3, temp[i-1]-1, cnt+1)

n = int(stdin.readline())
hp = list(map(int, stdin.readline().split()))
flag = max(hp)
for i in range(3- len(hp)):
    hp.append(0)
visit = [[[10**10]*(flag+1) for _ in range(flag+1)] for _ in range(flag+1)]
ans = 10**10
mutal(hp[0], hp[1], hp[2] , 0)
print(ans)