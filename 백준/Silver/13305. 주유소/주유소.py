#13305
from sys import stdin
n = int(stdin.readline())
l, p =[0 for i in range(n-1)], [0 for i in range(n)] #도로 길이 / 기름 가격
l[:], p[:] = map(int, input().split()), map(int, input().split())


f = l[0] * p[0] # 첫 거리를 가기 위해 무조건 필요함
minima = p[0]
for i in range(1, n-1):
    if(minima > p[i]):
        f += l[i] * p[i]
        minima = p[i]
    else:
        f += l[i] * minima
print(f)