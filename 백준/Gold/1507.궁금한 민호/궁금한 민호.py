#1507 궁금한 민호 
from sys import stdin
from copy import deepcopy
def func():
    cost = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if(i == j or i == k or j == k):
                    continue
                if(maps[i][j] + maps[j][k] < maps[i][k]):
                    print(-1)
                    exit()
                if(maps[i][j] + maps[j][k] == maps[i][k]):
                    temp[i][k] = 0

n = int(stdin.readline())
maps = [list(map(int,stdin.readline().split())) for _ in range(n)]
temp = deepcopy(maps)
ans = 0
func()
for i in range(n):
    for j in range(i+1,n):
        ans += temp[i][j]
print(ans)