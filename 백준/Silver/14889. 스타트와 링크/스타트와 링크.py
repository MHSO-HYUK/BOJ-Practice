# 14889 스타트와 링크
from sys import stdin
from itertools import combinations

n = int(stdin.readline())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
total = 0
for i in range(n):
    total += sum(maps[i])
minima = 10**10
for i in combinations(range(n), n//2):
    temp = 0
    dic = dict([p, 0] for p in range(n))
    for v in i:
        dic[v] = 1
    for k in range(len(i)):
        for j in range(k+1, len(i)):
            temp += maps[i[k]][i[j]]
            temp += maps[i[j]][i[k]]
    link, temp2 = [], 0
    for k in range(n):
        if not dic[k]:
            link.append(k)
    for k in link:
        for j in link:
            if k != j: temp2 += maps[k][j]

    minima = min(minima, abs(temp - temp2))
print(minima)