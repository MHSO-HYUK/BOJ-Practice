# 15686 치킨 배달
# 1 집 2 치킨 집
# 치킨 거리 = 집에 가장 가까운 치킨집 사이의 거리
# M개를 고르고 나머지 치킨 집은 모두 폐업시켜야 한다.
# 이때 치킨 거리가 가장 작게 되는 케이스의 치킨 거리의 최솟값을 구한다.
from sys import stdin
from itertools import combinations
def distance(home, store):
    return abs(home[0] - store[0]) + abs(home[1] - store[1])

n, m =map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
home, chick = [], []
num = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            home.append([i, j])
        if maps[i][j] == 2:
            chick.append([i, j])

            num += 1

minima = 10**10
for j in range(1, m+1):
    for k in combinations(range(num), j):
        temp2 = 0
        for q in home: # 각 집에 대해
            temp = 10**10
            for i in k: # 가장 가까운 치킨집 = 치킨 거리
                temp = min(temp, distance(q, chick[i]))
            temp2 += temp
        minima = min(minima, temp2)
print(minima)
