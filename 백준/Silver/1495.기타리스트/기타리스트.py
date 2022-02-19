#1495 기타리스트 
from sys import stdin
n, s, m = map(int, stdin.readline().split()) # s 시작볼륨 m 최대볼륨
vol = list(map(int, stdin.readline().split()))
check = [[0 for _ in range(m+1)] for _ in range(n+1)]
check[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if check[i][j]:
            if j + vol[i] <= m:
                check[i+1][j+vol[i]] = 1
            if j - vol[i] >= 0:
                check[i+1][j-vol[i]] = 1
                
flag = False
for i in range(m, -1, -1):
    if check[n][i] == 1:
        flag = True
        print(i)
        break
if not flag:
    print(-1) 